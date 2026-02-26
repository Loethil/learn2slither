from collections import defaultdict
import numpy as np
import random

class Agent:
    def __init__(self, QLoadPath: str, QSavePath: str):
        if QLoadPath:
            self.Qtable = self.loadQTable(QLoadPath)
        self.QSavePath = QSavePath
        self.Qtable = defaultdict(lambda: [0.0, 0.0, 0.0])
        self.epsilon: float = 1
        self.epsilonMin: float = 0.1
        self.epsilonDecay: float = 0.995
        self.gamma: float = 0.9
        self.alpha: float = 0.1


    def loadQTable(self, QLoadPath: str) -> dict:
        print(f"UNDER CONSTRUCT 'loadQTable': {QLoadPath}")

    
    def saveQTable(self, QSavePath: str) -> None:
        print(f"UNDER CONSTRUCT 'saveQTable': {QSavePath}")


    def decision(self, state: tuple[tuple])  -> int:
        if self.Qtable.get(state) is None:
            self.Qtable.update({state: [0.0, 0.0, 0.0]})
        if self.epsilon < np.random.rand() and np.max(self.Qtable[state]) != 0:
            action = np.argmax(self.Qtable[state])
        else:
            action = random.randint(0, 2)

        if self.epsilon > self.epsilonMin:
            self.epsilon *= self.epsilonDecay
        return action

    def learn(self, state, action, reward, next_state) -> None:
        target = reward + self.gamma * max(self.Qtable[next_state])
        self.Qtable[state][action] = self.Qtable[state][action] + self.alpha * (target - self.Qtable[state][action]) 
