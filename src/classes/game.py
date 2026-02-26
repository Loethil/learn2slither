import pygame
import time
from classes.environment import Env, RELATIVES
from classes.agent import Agent
from renderer import drawGrid, printBoard

CELL_SIZE = 50
GRID_WIDTH = 32
GRID_WEIGHT = 32

WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_WEIGHT * CELL_SIZE)


clock = pygame.time.Clock()

class Game:
    def __init__(self, boardXLength: int, boardYLength: int, snakeLength: int,
                 winCondition: int, visual: bool) -> None:
        self.boardXLength = boardXLength
        self.boardYLength = boardYLength
        self.snakeLength = snakeLength
        self.winCondition = winCondition
        self.visual = visual
        self.env = Env(boardXLength, boardYLength, snakeLength)
        self.agent = Agent(10)
        self.gen = 0
        self._running = True
        pygame.init()
        if self.visual:
            self.screen = pygame.display.set_mode(WINDOW_SIZE)
            self.screen.fill((0, 0, 0))


    def display(self) -> None:
        if self.visual:
            drawGrid(self.screen, self.env.board, CELL_SIZE)
            pygame.display.flip()
            clock.tick(10)
        else:
            printBoard(self.env.board)


    def onExecute(self) -> None:
        while(self._running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.onAgentDecision()
            self.display()
            time.sleep(0)


    def onAgentDecision(self):
        state = self.env.snake.vision
        action = self.agent.decision(state)
        current_dir = self.env.snake.direction
        absolute_dir = RELATIVES[current_dir][action]
        reward, lose = self.env.step(absolute_dir)
        self.env.refreshBoard()
        if lose:
            if self.env.snake.length != 0:
                next_state = self.env.getSnakeVision()
                self.agent.learn(state, action, reward, next_state)
            self.resetGame()
            return
        next_state = self.env.getSnakeVision()
        self.agent.learn(state, action, reward, next_state)
        self.env.snake.vision = next_state


    def onEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False


    def resetGame(self) -> None:
        self.env = Env(self.boardXLength, self.boardYLength, self.snakeLength)
        self.gen += 1
        print(f"Generation : {self.gen}")

    def onCleanup(self) -> None:
        pygame.quit()
        exit()