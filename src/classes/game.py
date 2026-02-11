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
        """"""
        self.env = Env(boardXLength, boardYLength, snakeLength)
        self.winCondition = winCondition
        pygame.init()
        self._running = True
        self.size = self.weight, self.height = 640, 400
        self.screen = pygame.display.set_mode(self.size)


    def onEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.env.snake.advance((0, -1))
            elif event.key == pygame.K_DOWN:
                self.env.snake.advance((0, 1))
            elif event.key == pygame.K_RIGHT:
                self.env.snake.advance((1, 0))
            elif event.key == pygame.K_LEFT:
                self.env.snake.advance((-1, 0))
            self.env.refreshBoard()
        if self.env.snake.length >= self.winCondition:
            print("YOU WIN ! CONGRATULATIONS !")
            exit()
        if self.env.snake.length == 0:
            print('GAME OVER')
            exit()


    def onCleanup(self) -> None:
        pygame.quit()


    def onExecute(self) -> None:
        printBoard(self.env.board)
        # self.snake.printVision()
        while(self._running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.screen.fill((0, 0, 0))
            drawGrid(self.screen, self.env.board, CELL_SIZE)
            pygame.display.flip()
            clock.tick(10)
        self.onCleanup()