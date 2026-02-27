import numpy as np
import random
from dataclasses import dataclass
from classes.snake import Snake
from utils import bucketize, randCol, randRow

RELATIVES = {
    (-1, 0): ((-1, 0), (0, -1), (0, 1)),   # va UP    : front=UP,    left=LEFT,  right=RIGHT
    (1, 0):  ((1, 0),  (0, 1),  (0, -1)),   # va DOWN  : front=DOWN,  left=RIGHT, right=LEFT
    (0, -1): ((0, -1), (1, 0),  (-1, 0)),   # va LEFT  : front=LEFT,  left=DOWN,  right=UP
    (0, 1):  ((0, 1),  (-1, 0), (1, 0)),    # va RIGHT : front=RIGHT, left=UP,    right=DOWN
}


@dataclass
class SnakeBody:
    value: str = 'S'
    x: int = 0
    y: int = 0


class Env:
    def __init__(self, boardSize, snakeLength) -> None:
        """"""
        self.boardSize: int = boardSize
        self.board: np.ndarray = self.createBoard()
        self.snakeLength = snakeLength
        self.snake: Snake = Snake(self.createSnakeBody())
        self.refreshBoard()
        self.snake.vision = self.getSnakeVision()
        self.addAppleOnBoard('G')
        self.addAppleOnBoard('G')
        self.addAppleOnBoard('R')


    def createBoard(self) -> np.ndarray:
        board = np.empty((self.boardSize, self.boardSize), dtype=str)
        for r in range(self.boardSize):
            for c in range (self.boardSize):
                board[r, c] = '0'
        for c in range(self.boardSize):
            board[0, c] = 'W'
            board[self.boardSize - 1, c] = 'W'
        for r in range(self.boardSize):
            board[r, 0] = 'W'
            board[r, self.boardSize - 1] = 'W'
        return board


    def addAppleOnBoard(self, appleType: str) -> None:
        newAppleX: int = randCol(self.boardSize)
        newAppleY: int = randRow(self.boardSize)
        
        if self.board[newAppleY, newAppleX] in ['R', 'G', 'H', 'S']:
            while self.board[newAppleY, newAppleX] != '0':
                newAppleX = randCol(self.boardSize)
                newAppleY = randRow(self.boardSize)
        self.board[newAppleY, newAppleX] = appleType


    def refreshBoard(self) -> None:
        for r in range(self.boardSize):
            for c in range (self.boardSize):
                if self.board[r, c] == 'H' or self.board[r, c] == 'S':
                    self.board[r, c] = '0'
        for bodyPart in self.snake.snakeBody:
            self.board[bodyPart.y, bodyPart.x] = bodyPart.value


    def createSnakeBody(self) -> list[SnakeBody]:
        newSnakeBody: list[SnakeBody] = []
        snakeX: int = randCol(self.boardSize)
        snakeY: int = randRow(self.boardSize)

        if self.board[snakeY, snakeX] in ['R', 'G', 'H', 'S', 'W']:
            while self.board[snakeY, snakeX] != '0':
                snakeX = randCol(self.boardSize)
                snakeY = randRow(self.boardSize)
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
            if 0 <= newBodyPartX < self.boardSize and 0 <= newBodyPartY < self.boardSize:
                if self.board[newBodyPartY, newBodyPartX] == '0':
                    self.board[newBodyPartY, newBodyPartX] = 'S'
                    return SnakeBody(value='S', x=newBodyPartX, y=newBodyPartY)


    def step(self, dir) -> tuple[float, bool]:
        nextY = self.snake.snakeBody[0].y + dir[0]
        nextX = self.snake.snakeBody[0].x + dir[1]
        snakeMeal = self.board[nextY, nextX]

        self.snake.advance(dir)
        self.refreshBoard()
        match snakeMeal:
            case 'W':
                return (-1.0, True)
            case 'S':
                return (-1.0, True)
            case 'G':
                self.snake.grow(self.addBodypartOnBoard(self.snake.snakeBody[-1]))
                self.addAppleOnBoard('G')
                return (1.0, False)
            case 'R':
                self.snake.shrink()
                self.addAppleOnBoard('R')
                if self.snake.length == 0:
                    return (-1.0, True)
                return (-0.5, False)
        return (-0.1, False)


    def look(self, start, delta) -> tuple:
        row, col = start
        distance = 0
        while True:
            row += delta[0]
            col += delta[1]
            distance += 1
            if row < 0 or row >= self.boardSize or col < 0 or col >= self.boardSize:
                return ('W', distance)
            cell = str(self.board[row, col])
            if cell != '0':
                return (cell, distance)


    def getSnakeVision(self) -> tuple[tuple]:
        snakeHead = [self.snake.snakeBody[0].y, self.snake.snakeBody[0].x]

        frontDir, leftDir, rightDir = RELATIVES[self.snake.direction]
        frontType, frontDist = self.look(snakeHead, frontDir)
        leftType,  leftDist  = self.look(snakeHead, leftDir)
        rightType, rightDist = self.look(snakeHead, rightDir)

        state = (
            (frontType, bucketize(frontDist)),
            (leftType,  bucketize(leftDist)),
            (rightType, bucketize(rightDist)),
        )
        return state
