from argparse import ArgumentParser
from classes.game import Game


def main() -> None:
    try:
        parser = ArgumentParser(prog="main")
        parser.add_argument("-sessions", type=int, help="number of sessions")
        parser.add_argument("-visual", action="store_true", help="visual interface, if False display in terminal")
        parser.add_argument("-dontlearn", action="store_true", help="prevents the model from training")
        parser.add_argument("-step-by-step", action="store_true", help="step by step visual for debugging purpose")
        parser.add_argument("-load", type=str, default="models/defaut.txt", help="save the model to a custom path")
        # args = parser.parse_args()
        game = Game(10, 10, 3, 10)
        game.onExecute()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()