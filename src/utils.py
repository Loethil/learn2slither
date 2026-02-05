import numpy as np
import os


def printBoard(environment, snake) -> None:
    # os.system('clear')
    for r in range(environment.x_length):
        for c in range (environment.y_length):
            if environment.board[r, c] == 'H' or environment.board[r, c] == 'S':
                environment.board[r, c] = '0'
    for bodyPart in snake.snakeBody:
        environment.board[bodyPart.y, bodyPart.x] = bodyPart.value
    for row in environment.board:
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
    

def randRow(y_length) -> int:
    return np.random.randint(1, y_length - 1)


def randCol(x_length) -> int:
    return np.random.randint(1, x_length - 1)