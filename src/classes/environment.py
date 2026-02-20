import numpy as np
import random
from dataclasses import dataclass
from classes.snake import Snake


def randRow(y) -> int:
    return np.random.randint(1, y - 1)


def randCol(x) -> int:
    return np.random.randint(1, x - 1)


@dataclass
class SnakeBody:
    value: str = 'S'
    x: int = 0
    y: int = 0


class Env:
    def __init__(self, boardX, boardY, snakeLength) -> None:
        """"""
        #BOARD
        self.boardX: int = boardX
        self.boardY: int  = boardY
        self.board: np.ndarray = self.createBoard()
        self.addAppleOnBoard('G')
        self.addAppleOnBoard('G')
        self.addAppleOnBoard('R')
        #SNAKE
        self.snakeLength = snakeLength
        self.snake: Snake = Snake(self.createSnakeBody())
        self.snake.vision = self.getSnakeVision()


    ###BOARD###
    def createBoard(self) -> np.ndarray:
        board = np.empty((self.boardY, self.boardX), dtype=str)
        for r in range(self.boardY):
            for c in range (self.boardX):
                board[r, c] = '0'
        for c in range(self.boardX):
            board[0, c] = 'W'
            board[self.boardY - 1, c] = 'W'
        for r in range(self.boardY):
            board[r, 0] = 'W'
            board[r, self.boardX - 1] = 'W'
        return board


    def addAppleOnBoard(self, appleType: str) -> None:
        newAppleX: int = randCol(self.boardX)
        newAppleY: int = randRow(self.boardY)
        
        if self.board[newAppleY, newAppleX] in ['R', 'G', 'H', 'S']:
            while self.board[newAppleY, newAppleX] != '0':
                newAppleX = randCol(self.boardX)
                newAppleY = randRow(self.boardY)
        self.board[newAppleY, newAppleX] = appleType


    def refreshBoard(self) -> None:
        for r in range(self.boardY):
            for c in range (self.boardX):
                if self.board[r, c] == 'H' or self.board[r, c] == 'S':
                    self.board[r, c] = '0'
        for bodyPart in self.snake.snakeBody:
            self.board[bodyPart.y, bodyPart.x] = bodyPart.value


    ###SNAKE###
    def createSnakeBody(self) -> list[SnakeBody]:
        newSnakeBody: list[SnakeBody] = []
        snakeX: int = randCol(self.boardX)
        snakeY: int = randRow(self.boardY)

        if self.board[snakeY, snakeX] in ['R', 'G', 'H', 'S', 'W']:
            while self.board[snakeY, snakeX] != '0':
                snakeX = randCol(self.boardX)
                snakeY = randRow(self.boardY)
        newSnakeBody.append(SnakeBody(value='H', x=snakeX, y=snakeY))
        self.board[snakeY, snakeX] = 'H'
        for _ in range(1, self.snakeLength, 1):
            newSnakeBody.append(self.addBodypartOnBoard(newSnakeBody[-1]))
        return newSnakeBody


    def addBodypartOnBoard(self, lastBodyPart: SnakeBody) -> SnakeBody:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            newBodyPartX, newBodyPartY = lastBodyPart.x + dx, lastBodyPart.y + dy
            if 0 <= newBodyPartX < self.boardX and 0 <= newBodyPartY < self.boardY:
                if self.board[newBodyPartY, newBodyPartX] == '0':
                    self.board[newBodyPartY, newBodyPartX] = 'S'
                    return SnakeBody(value='S', x=newBodyPartX, y=newBodyPartY)


    def getSnakeVision(self) -> tuple[tuple]:
        posX = self.snake.snakeBody[0].x
        posY = self.snake.snakeBody[0].y

        up = tuple(str(self.board[y][posX]) for y in range(posY - 1, -1, -1))
        down = tuple(str(self.board[y][posX]) for y in range(posY + 1, self.boardY))
        left = tuple(str(self.board[posY][x]) for x in range(posX - 1, -1, -1))
        right = tuple(str(self.board[posY][x]) for x in range(posX + 1, self.boardX))

        return (up, down, left, right)
