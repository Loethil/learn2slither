from utils import randCol, randRow
import os
import numpy as np

class Env:
    def __init__(self, x_length: int, y_length: int):
        self.x_length = x_length
        self.y_length = y_length
        
        self.board = self.createBoard(x_length, y_length)
        self.addAppleOnBoard('G')
        self.addAppleOnBoard('G')
        self.addAppleOnBoard('R')


    def createBoard(self, x_length: int, y_length: int) -> np.ndarray:
        if x_length < 10 or y_length < 10:
            raise ValueError("Board cannot be less than 10x10")
        board = np.empty((x_length, y_length), dtype=str)
        for r in range(x_length):
            for c in range (y_length):
                board[r, c] = '0'
                
        for c in range(x_length):
            board[0, c] = 'W'
            board[y_length - 1, c] = 'W'

        for r in range(y_length):
            board[r, 0] = 'W'
            board[r, x_length - 1] = 'W'

        return board


    def addAppleOnBoard(self, apple_type: str) -> None:
        if apple_type not in {'G', 'R'}:
            raise ValueError("apple_type must be one of {'G','R'}")

        new_apple_x: int = randCol(self.x_length)
        new_apple_y: int = randRow(self.y_length)
        
        while self.board[new_apple_y, new_apple_x] != '0':         
            new_apple_x = randCol(self.x_length)
            new_apple_y = randRow(self.y_length)
        self.board[new_apple_y, new_apple_x] = apple_type

    def refreshBoard(self, snake) -> np.ndarray:
        for r in range(self.x_length):
            for c in range (self.y_length):
                if self.board[r, c] == 'H' or self.board[r, c] == 'S':
                    self.board[r, c] = '0'
        for bodyPart in snake.snakeBody:
            self.board[bodyPart.y, bodyPart.x] = bodyPart.value

    def printBoard(self) -> None:
        os.system('clear')
        for row in self.board:
            for cell in row:
                match cell:
                    case 'W':
                        print(f"\033[33m{cell}\033[0m", end=' ')
                    case 'G':
                        print(f"\033[32m{cell}\033[0m", end=' ')
                    case 'R':
                        print(f"\033[31m{cell}\033[0m", end=' ')
                    case 'H':
                        print(f"\033[34m{cell}\033[0m", end=' ')
                    case 'S':
                        print(f"\033[36m{cell}\033[0m", end=' ')
                    case '0':
                        print(f"{cell}", end=' ')
            print()