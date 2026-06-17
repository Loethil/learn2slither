import pygame

def debugVision(board, snakeY, snakeX, snakeVision) -> None:
    print()
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if y == snakeY or x == snakeX:
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
            else:
                print(' ', end=' ')
        print()
    print(f"FRONT: {snakeVision[0]}, LEFT: {snakeVision[1]}, RIGHT: {snakeVision[2]}")
    print()

def printBoard(board) -> None:
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


# def drawGrid(screen, grid, CELL_SIZE) -> None:
#     for y, row in enumerate(grid):
#         for x, cell in enumerate(row):
#             color = [100, 100, 100]
#             if cell == 'W':
#                 color = [255, 255, 255] # Wall
#             elif cell == 'H':
#                 color = [123, 132, 0] # Snake head
#             elif cell == 'S':
#                 color = [0, 0, 255] # Snake body
#             elif cell == 'G':
#                 color = [0, 255, 0] # Green apple
#             elif cell == 'R':
#                 color = [255, 0, 0] # Red apple

#             rect = pygame.Rect(
#                 x * CELL_SIZE,
#                 y * CELL_SIZE,
#                 CELL_SIZE,
#                 CELL_SIZE
#             )
#             pygame.draw.rect(screen, color, rect)

#a Refaire
def drawGrid(screen, grid, CELL_SIZE) -> None:
    # Trouver les positions du serpent pour connecter les segments
    head_pos = None
    body_positions = set()
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'H':
                head_pos = (x, y)
            elif cell == 'S':
                body_positions.add((x, y))

    snake_positions = body_positions | ({head_pos} if head_pos else set())

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            rx = x * CELL_SIZE
            ry = y * CELL_SIZE

            # Fond de la cellule
            if cell == 'W':
                pygame.draw.rect(screen, (220, 220, 220), (rx, ry, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, (180, 180, 180), (rx, ry, CELL_SIZE, CELL_SIZE), 1)
                continue
            else:
                # Fond grille sombre élégant
                base_color = (30, 35, 40) if (x + y) % 2 == 0 else (33, 38, 44)
                pygame.draw.rect(screen, base_color, (rx, ry, CELL_SIZE, CELL_SIZE))

            if cell in ('H', 'S'):
                # Dessiner les connexions entre segments adjacents
                neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                for nx, ny in neighbors:
                    if (nx, ny) in snake_positions:
                        cx1 = rx + CELL_SIZE // 2
                        cy1 = ry + CELL_SIZE // 2
                        cx2 = nx * CELL_SIZE + CELL_SIZE // 2
                        cy2 = ny * CELL_SIZE + CELL_SIZE // 2
                        # Rectangle de connexion entre les deux centres
                        mid_rect = pygame.Rect(
                            min(cx1, cx2) - CELL_SIZE // 4,
                            min(cy1, cy2) - CELL_SIZE // 4,
                            abs(cx2 - cx1) + CELL_SIZE // 2,
                            abs(cy2 - cy1) + CELL_SIZE // 2,
                        )
                        conn_color = (80, 160, 60) if cell == 'H' else (50, 130, 40)
                        pygame.draw.rect(screen, conn_color, mid_rect)

                # Cercle principal du segment
                center = (rx + CELL_SIZE // 2, ry + CELL_SIZE // 2)
                radius = (CELL_SIZE // 2) - 2

                if cell == 'H':
                    # Tête : cercle vert vif avec yeux
                    pygame.draw.circle(screen, (100, 200, 70), center, radius)
                    pygame.draw.circle(screen, (70, 160, 50), center, radius, 2)

                    # Yeux (petits cercles blanCELL_SIZE avec pupilles)
                    eye_offset = radius // 3
                    for ex, ey in [(-eye_offset, -eye_offset // 2), (eye_offset, -eye_offset // 2)]:
                        eye_pos = (center[0] + ex, center[1] + ey)
                        pygame.draw.circle(screen, (255, 255, 255), eye_pos, max(2, radius // 5))
                        pygame.draw.circle(screen, (20, 20, 20), eye_pos, max(1, radius // 8))
                # else:
                #     # Corps : cercle vert légèrement plus sombre
                #     pygame.draw.circle(screen, (60, 150, 45), center, radius)
                #     pygame.draw.circle(screen, (40, 120, 30), center, radius, 2)

            elif cell == 'G':
                # Pomme verte : cercle avec reflet
                center = (rx + CELL_SIZE // 2, ry + CELL_SIZE // 2)
                radius = (CELL_SIZE // 2) - 3
                pygame.draw.circle(screen, (50, 200, 50), center, radius)
                pygame.draw.circle(screen, (30, 160, 30), center, radius, 2)
                # Reflet
                highlight = (center[0] - radius // 3, center[1] - radius // 3)
                pygame.draw.circle(screen, (150, 255, 150), highlight, max(2, radius // 4))
                # Petite tige
                stem_start = (center[0], center[1] - radius)
                stem_end = (center[0] + radius // 3, center[1] - radius - CELL_SIZE // 5)
                pygame.draw.line(screen, (100, 60, 20), stem_start, stem_end, 2)

            elif cell == 'R':
                # Pomme rouge : même style
                center = (rx + CELL_SIZE // 2, ry + CELL_SIZE // 2)
                radius = (CELL_SIZE // 2) - 3
                pygame.draw.circle(screen, (220, 50, 50), center, radius)
                pygame.draw.circle(screen, (180, 30, 30), center, radius, 2)
                highlight = (center[0] - radius // 3, center[1] - radius // 3)
                pygame.draw.circle(screen, (255, 160, 160), highlight, max(2, radius // 4))
                stem_start = (center[0], center[1] - radius)
                stem_end = (center[0] + radius // 3, center[1] - radius - CELL_SIZE // 5)
                pygame.draw.line(screen, (100, 60, 20), stem_start, stem_end, 2)