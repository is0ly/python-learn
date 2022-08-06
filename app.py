import numpy as np


def calculate_log(*args):
    return np.log(args)


print(calculate_log(22, 30))
print(calculate_log(1, 2, 3, 55))
print(calculate_log(12, 0.4, 55, 8))
