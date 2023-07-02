def gradient_descent(X, y, learning_rate, num_iterations):
    m = len(y)  # Number of training examples
    n = X.shape[1]  # Number of features
    theta = np.zeros(n)  # Initialize the parameter vector

    for iteration in range(num_iterations):
        gradients = (2 / m) * X.T.dot(X.dot(theta) - y)  # Compute gradients
        theta = theta - learning_rate * gradients  # Update parameters

    return theta
