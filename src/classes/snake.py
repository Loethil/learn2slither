from dataclasses import dataclass

@dataclass
class SnakeBody:
    value: str = 'S'
    x: int = 0
    y: int = 0

class Snake:
    def __init__(self, snakeBody: list[SnakeBody]):
        self.snakeBody: list[SnakeBody] = snakeBody
        self.length: int = len(snakeBody)
        self.vision = 0 # a implementer ou alors uniquement l'agent la ?
    

    #fonction pour avancer d'une case selon une direction donner
    def advance(self, dir: tuple[int, int]) -> None:
        for i in range(self.length - 1, -1, -1):
            if self.snakeBody[i].value == 'H':
                self.snakeBody[i].x += dir[0]
                self.snakeBody[i].y += dir[1]
            else:
                self.snakeBody[i].x = self.snakeBody[i - 1].x
                self.snakeBody[i].y = self.snakeBody[i - 1].y


    #fonction pour retrecir le snake
    def shrink(self) -> None:
        self.snakeBody.pop()
        self.length = len(self.snakeBody)


    #fonction pour agrandire le snake
    def grow(self, newBodyPart) -> None:
        self.snakeBody.append(newBodyPart)
        self.length = len(self.snakeBody)



    # def getVision(self, board: np.ndarray) -> dict[str, list]:
    #     posX = self.snakeBody[0].x
    #     posY = self.snakeBody[0].y

    #     return {
    #         'UP': [str(board[y][posX]) for y in range(posY - 1, -1, -1)],
    #         'DOWN': [str(board[y][posX]) for y in range(posY + 1, len(board))],
    #         'LEFT': [str(board[posY][x]) for x in range(posX - 1, -1, -1)],
    #         'RIGHT': [str(board[posY][x]) for x in range(posX + 1, len(board[posX]))]
    #     }
    

    # def printVision(self) -> None:
    #     """"""
    #     print(f"Up = {self.vision['UP']}")
    #     print(f"Down = {self.vision['DOWN']}")
    #     print(f"Left = {self.vision['LEFT']}")
    #     print(f"Right = {self.vision['RIGHT']}")
