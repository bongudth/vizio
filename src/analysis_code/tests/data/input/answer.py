# Python code to find smallest K-digit
# number divisible by X


def answer(X, K):
    # Computing MAX
    MIN = pow(10, K - 1)

    if MIN % X == 0:
        return MIN

    else:
        return (MIN + X) - ((MIN + X) % X)
