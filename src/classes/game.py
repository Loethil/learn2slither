from classes.snake import Snake
from classes.environment import Env
import keyboard


class Game:
    """"""
    def __init__(self, boardXLength: int, boardYLength: int, snakeLength: int, winCondition: int) -> None:
        """"""
        self.env = Env(boardXLength, boardYLength)
        self.snakeLength = snakeLength
        self.snake = Snake(self.env, self.snakeLength)
        self.winCondition = winCondition


    def gameLoop(self, snake: Snake, env: Env) -> None:
        env.printBoard()
        snake.printVision()
        while True:
            e = keyboard.read_event()
            if e.event_type == 'down':
                self.mouvmentEvent(snake, env, e.name)   
                sc = e.scan_code
                while True:
                    u = keyboard.read_event()
                    if u.event_type == 'up' and u.scan_code == sc:
                        break


    def mouvmentEvent(self, snake: Snake, env: Env, event: str) -> int:
        """"""
        dir: dict[tuple] = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
        theoretical_x = snake.snakeBody[0].x + dir[event][0]
        theoretical_y = snake.snakeBody[0].y + dir[event][1]
        next_step = env.board[theoretical_y, theoretical_x]
        if next_step == 'G':
            self.snakeEatGreenApple(self.snake, self.env)
        elif next_step == 'R':
            self.snakeEatRedApple(self.snake, self.env)
        elif next_step == 'W':
            print('GAME OVER')
            exit()
        snake.moveBody(dir[event])
        env.refreshBoard(snake)
        env.printBoard()
        snake.vision = snake.getVision(env.board)
        snake.printVision()


    def snakeEatGreenApple(self, snake: Snake, env: Env) -> int:
        """"""
        snake.addSnakeBodyOnBoard(env)
        snake.length += 1
        if len(snake.snakeBody) >= self.winCondition:
            print("YOU WIN ! CONGRATULATIONS !")
            exit()
        env.addAppleOnBoard('G')


    def snakeEatRedApple(self, snake: Snake, env: Env) -> int:
        """"""
        snake.snakeBody.pop()
        snake.length -= 1
        if len(snake.snakeBody) == 0:
            print('GAME OVER')
            exit()
        env.addAppleOnBoard('R')