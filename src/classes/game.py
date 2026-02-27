import pygame
import os
import time
from classes.environment import Env, RELATIVES
from classes.agent import Agent
from renderer import drawGrid, printBoard

CELL_SIZE = 50
GRID_WIDTH = 32
GRID_WEIGHT = 32

WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_WEIGHT * CELL_SIZE)

SNAKE_LENGTH = 3

clock = pygame.time.Clock()

class Game:
    def __init__(self, sessions: int,
                 visual: str,
                 dontLearn: bool, 
                 stepByStep: bool,
                 speed: int,
                 boardSize: int,
                 savePath: str,
                 loadPath: str) -> None:
        self.sessionsMax = sessions  # DONE
        self.sessions = 0            # DONE
        self.visual = visual         # DONE
        self.dontLearn = dontLearn   # DONE
        self.stepByStep = stepByStep 
        self.speed = speed           # DONE
        self.boardSize = boardSize   # DONE
        self.savePath = savePath     # DONE
        self.loadPath = loadPath     # DONE
        
        self.snakeLength = SNAKE_LENGTH
        self.env = Env(boardSize, SNAKE_LENGTH)
        self.agent = Agent(loadPath, savePath)
        
        if self.visual == "pygame":
            self.initPygame()


    def onExecute(self) -> None:
        while(self.sessions < self.sessionsMax):
            if self.visual == "pygame":
                for event in pygame.event.get():
                    self.onEvent(event)
            self.onAgentDecision()
            self.display()
            time.sleep(self.speed)
        if self.savePath:
            self.agent.saveQTable(self.savePath)


    def onAgentDecision(self):
        state = self.env.snake.vision
        action = self.agent.decision(state)

        absoluteDir = RELATIVES[self.env.snake.direction][action]
        reward, lose = self.env.step(absoluteDir)
        self.env.refreshBoard()

        if lose:
            if self.env.snake.length != 0:
                next_state = self.env.getSnakeVision()
                self.agent.learn(state, action, reward, next_state)
            self.resetGame()
            return

        next_state = self.env.getSnakeVision()
        if self.dontLearn is False:
            self.agent.learn(state, action, reward, next_state)
        self.env.snake.vision = next_state


    def resetGame(self) -> None:
        self.env = Env(self.boardSize, self.snakeLength)
        self.sessions += 1


    def display(self) -> None:
        if self.visual == "pygame":
            os.system('clear')
            print(f"SESSIONS: {self.sessions}/{self.sessionsMax}")
            drawGrid(self.screen, self.env.board, CELL_SIZE)
            pygame.display.flip()
            clock.tick(10)
        elif self.visual == "terminal":
            printBoard(self.env.board, self.sessions, self.sessionsMax)


    def onEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False


    def initPygame(self) -> None:
        self._running = True
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.screen.fill((0, 0, 0))


    def onCleanup(self) -> None:
        pygame.quit()
        exit()