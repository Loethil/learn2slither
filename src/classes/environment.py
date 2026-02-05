from utils import randCol, randRow
import numpy as np


class Environment:
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
