import numpy as np


def calculate(numbers):
    """Return mean, variance, standard deviation, max, min and sum of a 3x3 matrix.

    The input list of 9 numbers is turned into a 3x3 NumPy array.
    Each statistic is returned as a list of three items:
      [values along axis 0 (per column), values along axis 1 (per row), value for the whole matrix]
    """
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    def stats(func):
        return [
            func(matrix, axis=0).tolist(),  # down each column
            func(matrix, axis=1).tolist(),  # across each row
            func(matrix).tolist(),          # whole matrix (flattened)
        ]

    return {
        "mean": stats(np.mean),
        "variance": stats(np.var),
        "standard deviation": stats(np.std),
        "max": stats(np.max),
        "min": stats(np.min),
        "sum": stats(np.sum),
    }
