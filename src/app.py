def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def square(a):
    return a ** 2

def sqrt(a, tolerance=1e-10):
    if a < 0:
        raise ValueError("Square root of a negative number is not allowed.")
    if a == 0:
        return 0

    x = a
    while True:
        root = 0.5 * (x + a / x)
        if abs(root - x) < tolerance:
            return root
        x = root

def log(a, iterations=100):
    if a <= 0:
        raise ValueError("Logarithm input must be greater than 0.")

    x = (a - 1) / (a + 1)
    result = 0
    power = x

    for n in range(1, iterations * 2, 2):
        result += power / n
        power *= x * x

    return 2 * result

def sin(x, degrees=True, terms=10):
    if degrees:
        x = x * 3.141592653589793 / 180

    result = 0
    sign = 1
    factorial = 1
    power = x

    for i in range(1, 2 * terms, 2):
        result += sign * power / factorial
        sign *= -1
        power *= x * x
        factorial *= (i + 1) * (i + 2)

    return result

def cos(x, degrees=True, terms=10):
    if degrees:
        x = x * 3.141592653589793 / 180

    result = 1
    sign = -1
    factorial = 2
    power = x * x

    for i in range(2, 2 * terms, 2):
        result += sign * power / factorial
        sign *= -1
        power *= x * x
        factorial *= (i + 1) * (i + 2)

    return result

def percentage(a, b):
    if b == 0:
        raise ValueError("Cannot calculate percentage with denominator zero.")
    return (a / b) * 100