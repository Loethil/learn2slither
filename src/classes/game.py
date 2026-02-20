import pygame
import time
from classes.environment import Env
from classes.agent import Agent
from renderer import drawGrid, printBoard

CELL_SIZE = 50
GRID_WIDTH = 32
GRID_WEIGHT = 32

WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_WEIGHT * CELL_SIZE)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

clock = pygame.time.Clock()

#REGLER LE PROBLEME DES DEPLACEMENTS FIXE QUAND DIRECTIONS CHOISIS VERS COU DU SERPENT
class Game:
    def __init__(self, boardXLength: int, boardYLength: int, snakeLength: int, winCondition: int) -> None:
        self.boardXLength = boardXLength
        self.boardYLength = boardYLength
        self.snakeLength = snakeLength
        self.env = Env(boardXLength, boardYLength, snakeLength)
        self.winCondition = winCondition
        self.agent = Agent(10)
        pygame.init()
        self._running = True
        self.screen = pygame.display.set_mode(WINDOW_SIZE)


    def onExecute(self) -> None:
        self.screen.fill((0, 0, 0))
        while(self._running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.onAgentDecision()
            drawGrid(self.screen, self.env.board, CELL_SIZE)
            pygame.display.flip()
            clock.tick(10)
        self.onCleanup()


    def onAgentDecision(self) -> None:
        snakeMeal: str = ""
        direction = self.agent.decision(self.env.snake.vision)
        match direction:
            case 0:
                snakeMeal = self.onMoved(UP)
            case 1:
                snakeMeal = self.onMoved(DOWN)
            case 2:
                snakeMeal = self.onMoved(LEFT)
            case 3:
                snakeMeal = self.onMoved(RIGHT)
        self.checkWinLoseConditions(snakeMeal)
        self.env.refreshBoard()
        printBoard(self.env.board)
        self.env.snake.vision = self.env.getSnakeVision()
        time.sleep(0.3)


    def onEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False


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