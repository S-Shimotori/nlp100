from functools import reduce

def create(sequence, n):
    return list(map(lambda key: sequence[key:key + n], range(0, len(sequence) - n + 1)))
