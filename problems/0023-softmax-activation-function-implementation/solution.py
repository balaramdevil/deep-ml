import math

def softmax(scores: list[float]) -> list[float]:
    max_val = max(scores)
    softy_list = [math.exp(x-max_val) for x in scores]
    denom = sum(softy_list)
    answer = [x/denom for x in softy_list]
    return answer