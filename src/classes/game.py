import pygame
import time
from classes.environment import Env, RELATIVES
from classes.agent import Agent
from renderer import drawGrid, printBoard, debugVision

CELL_SIZE = 40
SNAKE_LENGTH = 3

clock = pygame.time.Clock()

class Game:
    def __init__(self, sessions: int,
                 visual: str,
                 dontLearn: bool, 
                 speed: int,
                 boardSize: int,
                 debug: bool,
                 savePath: str,
                 loadPath: str) -> None:
        self.sessionsMax = sessions
        self.sessions = 0
        self.visual = visual   
        self.dontLearn = dontLearn
        self.stepByStep = False
        self.speed = speed
        self.boardSize = boardSize
        self.debug = debug
        self.savePath = savePath   
        self.loadPath = loadPath

        self.snakeLength = SNAKE_LENGTH
        self.env = Env(boardSize, SNAKE_LENGTH)
        self.agent = Agent(loadPath, savePath)
        self.snakeMaxDuration = 0
        self.snakeMaxLength = 3

        self._running = True
        if self.visual == "pygame":
            self.initPygame()


    def initPygame(self) -> None:
        pygame.init()
        window_size = (self.boardSize * CELL_SIZE, self.boardSize * CELL_SIZE)
        self.screen = pygame.display.set_mode(window_size)
        self.screen.fill((0, 0, 0))


    def onExecute(self) -> None:
        self.display()
        print(f"SESSIONS: {self.sessions + 1}/{self.sessionsMax}")
        while self._running and self.sessions < self.sessionsMax:
            if self.visual == "pygame":
                self.handleInput()
            if not self._running:
                break
            lose = self.onAgentDecision()
            self.display()
            if lose:
                self.resetGame()
                self.display()
            if not self.stepByStep:
                time.sleep(self.speed)
        print(f"Game Over, max length = {self.snakeMaxLength}, max duration = {self.snakeMaxDuration}")
        if self.savePath:
            self.agent.saveQTable(self.savePath)


    def handleInput(self) -> None:
        if self.stepByStep:
            self._stepAdvance = False
            while self._running and self.stepByStep and not self._stepAdvance:
                for event in pygame.event.get():
                    self.onEvent(event)
                pygame.time.wait(10)
        else:
            for event in pygame.event.get():
                self.onEvent(event)


    def onEvent(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self._stepAdvance = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if self.stepByStep:
                self.stepByStep = False
            else:
                self.stepByStep = True
            print(self.stepByStep)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self._running = False


    def onAgentDecision(self) -> bool:
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
            return True
        self.env.snake.duration += 1
        return False


    def resetGame(self) -> None:
        if self.snakeMaxLength < self.env.snake.length:
            self.snakeMaxLength = self.env.snake.length
        if self.snakeMaxDuration < self.env.snake.duration:
            self.snakeMaxDuration = self.env.snake.duration
        self.env = Env(self.boardSize, self.snakeLength)
        self.sessions += 1
        print(f"SESSIONS: {self.sessions + 1}/{self.sessionsMax}")


    def display(self) -> None:
        if self.visual == "pygame":
            drawGrid(self.screen, self.env.board, CELL_SIZE)
            pygame.display.flip()
            clock.tick(10)
        elif self.visual == "terminal":
            printBoard(self.env.board)
        if self.debug:
            debugVision(self.env.board, self.env.snake.headY, self.env.snake.headX, self.env.snake.vision)


    def onCleanup(self) -> None:
        pygame.quit()
        exit()