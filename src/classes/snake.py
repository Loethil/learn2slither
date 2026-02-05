from dataclasses import dataclass
from classes.environment import Environment
from utils import randCol, randRow, printBoard
import random

EMPTY = 0
GREEN_APPLE = 1
RED_APPLE = 2
WIN = 3
GAME_OVER = 4

@dataclass
class SnakeBody:
    value: str = 'S'
    x: int = 0
    y: int = 0


class Snake:
    def __init__(self, environment: Environment, length: int, win_condition: int):
        self.environment = environment
        self.snakeBody: list[SnakeBody] = []
        self.vision: dict[list] = {"UP": [], "DOWN": [], "RIGHT": [], "LEFT": []}
        self.length = length
        self.win_condition = win_condition
        self.createSnake(self.environment)


    def createSnake(self, environment: Environment) -> None:
        """"""
        snake_x: int = randCol(environment.x_length)
        snake_y: int = randRow(environment.y_length)
        
        self.snakeBody.append(SnakeBody(value='H', x=snake_x, y=snake_y))
        environment.board[snake_y, snake_x] = 'H'
        for _ in range(1, self.length, 1):
            snake_x, snake_y = self.addSnakeBodyOnBoard(environment)
        return self
    

    def addSnakeBodyOnBoard(self, environment: Environment) -> None: # a changer pour toujours spawn dans l'alignement du serpent
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # droite, gauche, bas, haut
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = self.snakeBody[-1].x + dx, self.snakeBody[-1].y + dy
            if 0 <= nx < environment.x_length and 0 <= ny < environment.y_length:
                if environment.board[ny, nx] == '0':
                    self.snakeBody.append(SnakeBody(value='S', x=nx, y=ny))
                    environment.board[ny, nx] = 'S'
                    return nx, ny


    def getVision(self, board: list[list]) -> None:
        """Snake Vision state"""
        pos_x = self.snakeBody[0].x
        pos_y = self.snakeBody[0].y

        self.vision = {
            'UP': [board[i][pos_y] for i in range(pos_x - 1, -1, -1)],
            'DOWN': [board[i][pos_y] for i in range(pos_x + 1, len(board))],
            'LEFT': [board[pos_x][j] for j in range(pos_y - 1, -1, -1)],
            'RIGHT': [board[pos_x][j] for j in range(pos_y + 1, len(board[pos_x]))]
        }
        print(f"Up = {self.vision['UP']}")
        print(f"Down = {self.vision['DOWN']}")
        print(f"Left = {self.vision['LEFT']}")
        print(f"Right = {self.vision['RIGHT']}")


    def moveBody(self, board: list[list], dir: tuple) -> None:
        for i in range(len(self.snakeBody) - 1, -1, -1):
            if self.snakeBody[i].value == 'H':
                self.snakeBody[i].x += dir[0]
                self.snakeBody[i].y += dir[1]
            else:
                self.snakeBody[i].x = self.snakeBody[i - 1].x
                self.snakeBody[i].y = self.snakeBody[i - 1].y
        self.vision = self.getVision(board)



    def mouvmentEvent(self, environment: Environment, event: str) -> int:
        dir: dict[tuple] = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        theoretical_x = self.snakeBody[0].x + dir[event][0]
        theoretical_y = self.snakeBody[0].y + dir[event][1]
        next_step = environment.board[theoretical_y, theoretical_x]
        if next_step == 'G':
            self.moveBody(environment.board, dir[event])
            self.addSnakeBodyOnBoard(environment)
            if len(self.snakeBody) >= self.win_condition:
                return WIN
            environment.addAppleOnBoard('G')
            printBoard(environment, self)
            return GREEN_APPLE
        elif next_step == 'R':
            self.moveBody(environment.board, dir[event])
            self.snakeBody.pop()
            if len(self.snakeBody) == 0:
                return GAME_OVER
            environment.addAppleOnBoard('R')
            printBoard(environment, self)
            return RED_APPLE
        elif next_step == '0':
            self.moveBody(environment.board, dir[event])
            printBoard(environment, self)
            return EMPTY
        else:
            return GAME_OVER
