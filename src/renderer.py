import os
import pygame

def printBoard(board) -> None:
    os.system('clear')
    for row in board:
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


def drawGrid(screen, grid, CELL_SIZE) -> None:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color = [0, 0, 0]
            if cell == 'W':
                color = [255, 255, 255] # Wall
            elif cell == 'H':
                color = [123, 132, 0] # Snake head
            elif cell == 'S':
                color = [0, 0, 255] # Snake body
            elif cell == 'G':
                color = [0, 255, 0] # Green apple
            elif cell == 'R':
                color = [255, 0, 0] # Red apple

            rect = pygame.Rect(
                x * CELL_SIZE,
                y * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, color, rect)