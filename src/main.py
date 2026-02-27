from argparse import ArgumentParser
from classes.game import Game

def main() -> None:
    # try:
        parser = ArgumentParser(prog="main")
        parser.add_argument("-sessions", type=int, default=10, help="Number of sessions")
        parser.add_argument("-visual", type=str, choices=["pygame", "terminal", "none"], default="none", help="Visual interface, choose Pyagem, terminal or none")
        parser.add_argument("-dontLearn", action="store_true", help="Prevents the model from training")
        parser.add_argument("-stepByStep", action="store_true", help="Step by step visual for debugging purpose")
        parser.add_argument("-speed", type=float, default=0.0, help="Define the number of time (in second) between each action")
        parser.add_argument("-boardSize", type=int, choices=[10, 15, 20, 25], default=10, help="Size of the board")
        parser.add_argument("-save", type=str, help="Path for saving the model")
        parser.add_argument("-load", type=str, help="Load an existing model for testing it")
        args = parser.parse_args()
        game = Game(args.sessions,
                    args.visual,
                    args.dontLearn,
                    args.stepByStep,
                    args.speed,
                    args.boardSize,
                    args.save,
                    args.load)
        game.onExecute()

    # except Exception as e:
    #     print(f"Error: {e}")


if __name__ == "__main__":
    main()