import re
import numpy as np


def calculate_data_from_vectors(*args):
    result = []
    for arg in args:
        result.append(
            np.log(np.e ** (1 / (np.sin(arg) + 1)) / (5 / 4 + arg**5))
            / np.log(1 + arg**2)
        )
    return result


print(calculate_data_from_vectors(2, 23, 33))
