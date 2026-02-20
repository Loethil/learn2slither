import pygame
from classes.environment import Env
from renderer import drawGrid, printBoard, printSnakeVision

CELL_SIZE = 50
GRID_WIDTH = 32
GRID_WEIGHT = 32

WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_WEIGHT * CELL_SIZE)

clock = pygame.time.Clock()


class Game:
    def __init__(self, boardXLength: int, boardYLength: int, snakeLength: int, winCondition: int) -> None:
        self.boardXLength = boardXLength
        self.boardYLength = boardYLength
        self.snakeLength = snakeLength
        self.env = Env(boardXLength, boardYLength, snakeLength)
        self.winCondition = winCondition
        pygame.init()
        self._running = True
        self.screen = pygame.display.set_mode(WINDOW_SIZE)


    def onExecute(self) -> None:
        printBoard(self.env.board)
        printSnakeVision(self.env.snake.vision)
        while(self._running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.screen.fill((0, 0, 0))
            drawGrid(self.screen, self.env.board, CELL_SIZE)
            pygame.display.flip()
            clock.tick(10)
        self.onCleanup()


    def onEvent(self, event) -> None:
        snakeMeal: str = ""
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakeMeal = self.onMoved((0, -1))
            elif event.key == pygame.K_DOWN:
                snakeMeal = self.onMoved((0, 1))
            elif event.key == pygame.K_RIGHT:
                snakeMeal = self.onMoved((1, 0))
            elif event.key == pygame.K_LEFT:
                snakeMeal = self.onMoved((-1, 0))
            self.checkWinLoseConditions(snakeMeal)
            self.env.refreshBoard()
            self.env.snake.vision = self.env.getSnakeVision()
            printBoard(self.env.board)
            printSnakeVision(self.env.snake.vision)


    def onMoved(self, dir: tuple[int, int]) -> str:
        nextX = self.env.snake.snakeBody[0].x + dir[0]
        nextY = self.env.snake.snakeBody[0].y + dir[1]
        if self.env.snake.length > 1:
            if nextX == self.env.snake.snakeBody[1].x and nextY == self.env.snake.snakeBody[1].y:
                return
        if self.env.board[nextY, nextX] == 'G':
            self.env.snake.grow(self.env.addBodypartOnBoard(self.env.snake.snakeBody[-1]))
            self.env.addAppleOnBoard('G')
        elif self.env.board[nextY, nextX] == 'R':
            self.env.snake.shrink()
            self.env.addAppleOnBoard('R')
        self.env.snake.advance(dir)
        return (self.env.board[nextY, nextX])


    def checkWinLoseConditions(self, snakeMeal: str) -> None:
        if snakeMeal == 'W' or snakeMeal == 'S' or self.env.snake.length >= self.winCondition or self.env.snake.length == 0:
            self.resetGame()


    def resetGame(self) -> None:
        self.env = Env(self.boardXLength, self.boardYLength, self.snakeLength)


    def onCleanup(self) -> None:
        pygame.quit()
        exit()