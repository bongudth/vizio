import numpy as np


def linear_regression(X, y):
    X = np.array(X)
    y = np.array(y)
    X = np.c_[
        np.ones(X.shape[0]), X
    ]  # Add a column of ones to X for the intercept term
    w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)  # Compute the optimal weight vector
    return w
