import numpy as np

def bucketize(distance) -> str:
    if distance == 1:
        return 'close'
    elif distance <= 4:
        return 'medium'
    else:
        return 'far'
    
def randRow(y) -> int:
    return np.random.randint(1, y - 1)


def randCol(x) -> int:
    return np.random.randint(1, x - 1)
