import numpy as np


def randRow(y_length) -> int:
    return np.random.randint(1, y_length - 1)


def randCol(x_length) -> int:
    return np.random.randint(1, x_length - 1)