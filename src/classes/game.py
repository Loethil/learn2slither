from classes.snake import Snake
from classes.environment import Env
import pygame

CELL_SIZE = 50
GRID_WIDTH = 32
GRID_WEIGHT = 32

WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_WEIGHT * CELL_SIZE)

clock = pygame.time.Clock()


class Game:
    def __init__(self, boardXLength: int, boardYLength: int, snakeLength: int, winCondition: int) -> None:
        """"""
        self.env = Env(boardXLength, boardYLength)
        self.snakeLength = snakeLength
        self.snake = Snake(self.env, self.snakeLength)
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
                self.snake.mouvmentEvent("up")
            elif event.key == pygame.K_DOWN:
                self.snake.mouvmentEvent("down")
            elif event.key == pygame.K_RIGHT:
                self.snake.mouvmentEvent("right")
            elif event.key == pygame.K_LEFT:
                self.snake.mouvmentEvent("left")
        if self.snake.length >= self.winCondition:
            print("YOU WIN ! CONGRATULATIONS !")
            exit()
        if self.snake.length == 0:
            print('GAME OVER')
            exit()


    def onCleanup(self) -> None:
        pygame.quit()


    def onExecute(self) -> None:
        self.env.printBoard()
        self.snake.printVision()
        while(self._running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.screen.fill((0, 0, 0))
            self.drawGrid(self.screen, self.env.board)
            pygame.display.flip()
            clock.tick(10)
        self.onCleanup()

    
    def drawGrid(self, screen, grid) -> None:
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                color = [0, 0, 0]
                if cell == 'W':
                    color = [255, 255, 255] # Wall
                elif cell == 'H':
                    color = [123, 132, 0] # Snake head
                elif cell == 'S':
                    color = [0, 0, 255] # Snake body
                elif cell == 'G':
                    color = [0, 255, 0] # Green apple
                elif cell == 'R':
                    color = [255, 0, 0] # Red apple

                rect = pygame.Rect(
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(screen, color, rect)