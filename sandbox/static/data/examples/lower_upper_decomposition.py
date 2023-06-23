import numpy as np


def lower_upper_decomposition(table: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Ensure that table is a square array
    rows, columns = np.shape(table)
    if rows != columns:
        msg = (
            "'table' has to be of square shaped array but got a "
            f"{rows}x{columns} array:\n{table}"
        )
        raise ValueError(msg)

    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))
    for i in range(columns):
        for j in range(i):
            total = sum(lower[i][k] * upper[k][j] for k in range(j))
            if upper[j][j] == 0:
                raise ArithmeticError("No LU decomposition exists")
            lower[i][j] = (table[i][j] - total) / upper[j][j]
        lower[i][i] = 1
        for j in range(i, columns):
            total = sum(lower[i][k] * upper[k][j] for k in range(j))
            upper[i][j] = table[i][j] - total
    return lower, upper
