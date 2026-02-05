from argparse import ArgumentParser
from classes.environment import Environment
from classes.snake import Snake
from utils import printBoard
import keyboard

EMPTY = 0
GREEN_APPLE = 1
RED_APPLE = 2
WIN = 3
GAME_OVER = 4

def main() -> None:
    try:
        parser = ArgumentParser(prog="main")
        parser.add_argument("-sessions", type=int, help="number of sessions")
        parser.add_argument("-visual", action="store_true", help="visual interface, if False display in terminal")
        parser.add_argument("-dontlearn", action="store_true", help="prevents the model from training")
        parser.add_argument("-step-by-step", action="store_true", help="step by step visual for debugging purpose")
        parser.add_argument("-load", type=str, default="models/defaut.txt", help="save the model to a custom path")
        # args = parser.parse_args()
        environment: Environment = Environment(10, 10)
        snake: Snake = Snake(environment, 3, 10)
        printBoard(environment, snake)

        while True:
            e = keyboard.read_event()
            if e.event_type == 'down':
                result = snake.mouvmentEvent(environment, e.name)
                print(snake.vision)
                if result == GAME_OVER:
                    print('GAME OVER')
                    break
                elif result == WIN:
                    print("YOU WIN ! CONGRATULATIONS !")
                    exit()
                sc = e.scan_code
                while True:
                    u = keyboard.read_event()
                    if u.event_type == 'up' and u.scan_code == sc:
                        break

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()