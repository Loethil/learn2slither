from collections import defaultdict
import numpy as np
import random
import pickle

class Agent:
    def __init__(self, QLoadPath: str, QSavePath: str):
        self.epsilon: float = 1
        self.epsilonMin: float = 0.1
        self.epsilonDecay: float = 0.995
        self.gamma: float = 0.9
        self.alpha: float = 0.1
        if QLoadPath:
            self.loadQTable(QLoadPath)
        else:
            self.Qtable = defaultdict(lambda: [0.0, 0.0, 0.0])
        self.QSavePath = QSavePath


    def loadQTable(self, QLoadPath: str) -> None:
        with open(QLoadPath, 'rb') as f:
            data = pickle.load(f)
            self.Qtable = defaultdict(lambda: [0.0, 0.0, 0.0], data['qtable'])
            self.epsilon = data['epsilon']
        print(f"Load trained model from {QLoadPath}")

    def saveQTable(self, QSavePath: str) -> None:
        data = {'qtable': dict(self.Qtable),
                'epsilon': self.epsilon}
        with open(QSavePath, 'wb') as f:
            pickle.dump(data, f)
        print(f"Save learning state in {QSavePath}")


    def decision(self, state: tuple[tuple])  -> int:
        if self.Qtable.get(state) is None:
            self.Qtable.update({state: [0.0, 0.0, 0.0]})
        if self.epsilon < np.random.rand() and np.max(self.Qtable[state]) != 0:
            action = np.argmax(self.Qtable[state])
        else:
            # print("random")
            action = random.randint(0, 2)

        if self.epsilon > self.epsilonMin:
            self.epsilon *= self.epsilonDecay
        return action

    def learn(self, state, action, reward, next_state) -> None:
        target = reward + self.gamma * max(self.Qtable[next_state])
        self.Qtable[state][action] = self.Qtable[state][action] + self.alpha * (target - self.Qtable[state][action]) 
