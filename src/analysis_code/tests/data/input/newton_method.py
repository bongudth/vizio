def newton_method(f, f_prime, x0, max_iterations, tolerance):
    x = x0
    for iteration in range(max_iterations):
        fx = f(x)
        if abs(fx) < tolerance:
            return x
        f_prime_x = f_prime(x)
        if f_prime_x == 0:
            break
        x = x - fx / f_prime_x
    return None
