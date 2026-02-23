from dataclasses import dataclass

@dataclass
class SnakeBody:
    value: str = 'S'
    x: int = 0
    y: int = 0

class Snake:
    def __init__(self, snakeBody: list[SnakeBody]):
        self.snakeBody: list[SnakeBody] = snakeBody
        self.direction: tuple[int, int] = self.getBaseDirection()
        self.length: int = len(snakeBody)
        self.vision = None
    

    def advance(self, dir: tuple[int, int]) -> None:
        for i in range(self.length - 1, -1, -1):
            if self.snakeBody[i].value == 'H':
                self.snakeBody[i].y += dir[0]
                self.snakeBody[i].x += dir[1]
                self.direction = dir
            else:
                self.snakeBody[i].y = self.snakeBody[i - 1].y
                self.snakeBody[i].x = self.snakeBody[i - 1].x


    def shrink(self) -> None:
        self.snakeBody.pop()
        self.length = len(self.snakeBody)


    def grow(self, newBodyPart) -> None:
        self.snakeBody.append(newBodyPart)
        self.length = len(self.snakeBody)


    def getBaseDirection(self) -> tuple [int, int]:
        return (self.snakeBody[0].y - self.snakeBody[1].y, self.snakeBody[0].x - self.snakeBody[1].x)