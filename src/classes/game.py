import pygame
import os
import time
from classes.environment import Env, RELATIVES
from classes.agent import Agent
from renderer import drawGrid, printBoard

CELL_SIZE = 40
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
        self.sessionsMax = sessions
        self.sessions = 0         
        self.visual = visual   
        self.dontLearn = dontLearn
        self.stepByStep = stepByStep #NOT IMPLEMENTED
        self.speed = speed
        self.boardSize = boardSize
        self.savePath = savePath   
        self.loadPath = loadPath

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

        next_state = self.env.getSnakeVision()
        if self.dontLearn is False:
            self.agent.learn(state, action, reward, next_state)
        self.env.snake.vision = next_state

        if lose:
            self.resetGame()


    def resetGame(self) -> None:
        self.env = Env(self.boardSize, self.snakeLength)
        self.sessions += 1


    def display(self) -> None:
        os.system('clear')
        print(f"SESSIONS: {self.sessions}/{self.sessionsMax}")
        if self.visual == "pygame":
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
        window_size = (self.boardSize * CELL_SIZE, self.boardSize * CELL_SIZE)
        self.screen = pygame.display.set_mode(window_size)
        self.screen.fill((0, 0, 0))


    def onCleanup(self) -> None:
        pygame.quit()
        exit()