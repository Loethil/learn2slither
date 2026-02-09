from dataclasses import dataclass
from utils import randCol, randRow
import random
import numpy as np


@dataclass
class SnakeBody:
    value: str = 'S'
    x: int = 0
    y: int = 0


class Snake:
    def __init__(self, env, length: int) -> None:
        """"""
        self.env = env
        self.snakeBody: list[SnakeBody] = []
        self.length = length
        self.createSnake(self.env)
        self.vision: dict[str, list] = self.getVision(env.board)


    def createSnake(self, env) -> None:
        """"""
        snake_x: int = randCol(env.x_length)
        snake_y: int = randRow(env.y_length)
        
        self.snakeBody.append(SnakeBody(value='H', x=snake_x, y=snake_y))
        env.board[snake_y, snake_x] = 'H'
        for _ in range(1, self.length, 1):
            self.addSnakeBodyOnBoard(env)
    

    def addSnakeBodyOnBoard(self, env) -> None:
        """"""
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # droite, gauche, bas, haut
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = self.snakeBody[-1].x + dx, self.snakeBody[-1].y + dy
            if 0 <= nx < env.x_length and 0 <= ny < env.y_length:
                if env.board[ny, nx] == '0':
                    self.snakeBody.append(SnakeBody(value='S', x=nx, y=ny))
                    env.board[ny, nx] = 'S'
                    break


    def mouvmentEvent(self, event: str) -> int:
        """Trouver un moyen pour qu'il ne puisse pas allez dans la direction de son cou"""
        dir: dict[tuple] = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        theoretical_x = self.snakeBody[0].x + dir[event][0]
        theoretical_y = self.snakeBody[0].y + dir[event][1]
        next_step = self.env.board[theoretical_y, theoretical_x]
        if next_step == 'G' or next_step == 'R':
            self.snakeEatApple(next_step) 
        elif next_step != '0':
            print('GAME OVER')
            exit()
        self.moveBody(dir[event])
        self.env.refreshBoard(self)
        self.env.printBoard()
        self.vision = self.getVision(self.env.board)
        self.printVision()


    def moveBody(self, dir) -> None:
        """"""
        for i in range(len(self.snakeBody) - 1, -1, -1):
            if self.snakeBody[i].value == 'H':
                self.snakeBody[i].x += dir[0]
                self.snakeBody[i].y += dir[1]
            else:
                self.snakeBody[i].x = self.snakeBody[i - 1].x
                self.snakeBody[i].y = self.snakeBody[i - 1].y


    def snakeEatApple(self, apple: str) -> int:
        """"""
        if apple == 'G':
            self.addSnakeBodyOnBoard(self.env)
            self.length += 1
            self.env.addAppleOnBoard('G') #sometime dont spawn
        elif apple == 'R':
            self.snakeBody.pop()
            self.length -= 1
            self.env.addAppleOnBoard('R') #sometime dont spawn


    def getVision(self, board: np.ndarray) -> dict[str, list]:
        posX = self.snakeBody[0].x
        posY = self.snakeBody[0].y

        return {
            'UP': [str(board[y][posX]) for y in range(posY - 1, -1, -1)],
            'DOWN': [str(board[y][posX]) for y in range(posY + 1, len(board))],
            'LEFT': [str(board[posY][x]) for x in range(posX - 1, -1, -1)],
            'RIGHT': [str(board[posY][x]) for x in range(posX + 1, len(board[posX]))]
        }
    

    def printVision(self) -> None:
        """"""
        print(f"Up = {self.vision['UP']}")
        print(f"Down = {self.vision['DOWN']}")
        print(f"Left = {self.vision['LEFT']}")
        print(f"Right = {self.vision['RIGHT']}")
