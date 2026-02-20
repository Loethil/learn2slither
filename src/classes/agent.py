from collections import defaultdict
import numpy as np
import random

class Agent:
    def __init__(self, episode: int):
        self.Qtable = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0])
        self.epsilon: float = 1
        self.epsilonMin: float = 0.1
        self.episode: int = episode
        self.gamma: float = 0.9
        self.alpha: float = 0.99

    def decision(self, state: tuple[tuple])  -> tuple[int, int]:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if self.epsilon < np.random.rand() and np.max(self.Qtable[state]) != 0:
            action = directions[np.argmax(self.Qtable[state])]
        else:
            action = random.choice(directions)

        if self.epsilon > self.epsilonMin:
            self.epsilon *= self.alpha
        return action
