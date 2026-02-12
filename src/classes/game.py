import pygame
from classes.environment import Env
from renderer import drawGrid, printBoard

CELL_SIZE = 50
GRID_WIDTH = 32
GRID_WEIGHT = 32

WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_WEIGHT * CELL_SIZE)

clock = pygame.time.Clock()


class Game:
    def __init__(self, boardXLength: int, boardYLength: int, snakeLength: int, winCondition: int) -> None:
        self.env = Env(boardXLength, boardYLength, snakeLength)
        self.winCondition = winCondition
        pygame.init()
        self._running = True
        self.screen = pygame.display.set_mode(WINDOW_SIZE)


    def onMoved(self, dir: tuple[int, int]) -> None:
        nextX = self.env.snake.snakeBody[0].x + dir[0]
        nextY = self.env.snake.snakeBody[0].y + dir[1]
        if self.env.snake.length > 1:
            if nextX == self.env.snake.snakeBody[1].x and nextY == self.env.snake.snakeBody[1].y:
                return
        if self.env.board[nextY, nextX] == 'W' or self.env.board[nextY, nextX] == 'S':
            print("YOU LOSE! GAME OVER")
            self.onCleanup()
        elif self.env.board[nextY, nextX] == 'G':
            self.env.snake.grow(self.env.addBodypartOnBoard(self.env.snake.snakeBody[-1]))
            self.env.addAppleOnBoard('G')
            if self.env.snake.length >= self.winCondition:
                print("YOU WIN ! CONGRATULATIONS")
                self.onCleanup()
        elif self.env.board[nextY, nextX] == 'R':
            self.env.snake.shrink()
            self.env.addAppleOnBoard('R')
            if self.env.snake.length == 0:
                print("YOU LOSE! GAME OVER")
                self.onCleanup()
        self.env.snake.advance(dir)


    def onEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.onMoved((0, -1))
            elif event.key == pygame.K_DOWN:
                self.onMoved((0, 1))
            elif event.key == pygame.K_RIGHT:
                self.onMoved((1, 0))
            elif event.key == pygame.K_LEFT:
                self.onMoved((-1, 0))
            self.env.refreshBoard()
            printBoard(self.env.board)


    def onCleanup(self) -> None:
        pygame.quit()
        exit()


    def onExecute(self) -> None:
        printBoard(self.env.board)
        while(self._running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.screen.fill((0, 0, 0))
            drawGrid(self.screen, self.env.board, CELL_SIZE)
            pygame.display.flip()
            clock.tick(10)
        self.onCleanup()