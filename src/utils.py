def bucketize(distance) -> str:
    if distance == 1:
        return 'close'
    elif distance <= 4:
        return 'medium'
    else:
        return 'far'