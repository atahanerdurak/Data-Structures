test0 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [3, 4, 2]
    },
    'output': [6, 8, 19, 41, 38, 14]
}
test1 = {
    'input': {
        'poly1': [0, 0, 0, 0],
        'poly2': [1, 2, 3]
    },
    'output': [0, 0, 0, 0, 0, 0]
}
test2 = {
    'input': {
        'poly1': [5],
        'poly2': [2]
    },
    'output': [10]
}
test3 = {
    'input': {
        'poly1': [],
        'poly2': [1, 2, 3]
    },
    'output': []
}
test4 = {
    'input': {
        'poly1': [2, -4, 6],
        'poly2': [-3, 5, -2]
    },
    'output': [-6, 22, -42, 38, -12]
}
test5 = {
    'input': {
        'poly1': [1.5, -2.75, 3.25],
        'poly2': [0.5, 1.25, -2.75]
    },
    'output': [0.75, 0.5, -5.9375, 11.625, -8.9375]
}
test6 = {
    'input': {
        'poly1': [1, 2],
        'poly2': [0, 4]
    },
    'output': [0, 4, 8]
}

tests = [ test0, test1, test2, test3, test4, test5]


def multiply_basic(poly1, poly2):
    """Multiply two polynomials basically"""
    if len(poly1) == 0 or len(poly2) == 0:
        return []
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            coefs = poly1[i] * poly2[j]
            result[i + j] += coefs
    return result


def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result


def subtract(poly1, poly2):
    """Subtract two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] -= poly2[i]
    return result


def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])


def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly


def multiply_optimized(poly1, poly2):
    if not poly1 or not poly2:
        return []

    if len(poly1) == 1 or len(poly2) == 1:
        return [coeff_poly1 * coeff_poly2 for coeff_poly1 in poly1 for coeff_poly2 in poly2]

    (A0, A1), (B0, B1) = split(poly1, poly2)
    U = multiply_optimized(A0, B0)
    Z = multiply_optimized(A1, B1)
    Y = multiply_optimized(add(A0, A1), add(B0, B1))
    W = subtract(Y, add(U, Z))
    Z_increased = increase_exponent(Z, max(len(poly1), len(poly2)) // 2 * 2)
    W_increased = increase_exponent(W, max(len(poly1), len(poly2)) // 2)
    return add(add(U,Z_increased), W_increased)


for test in tests:
    print(multiply_optimized(**test['input']) == test['output'])
    print(multiply_optimized(**test['input']))
    print(test['output'])
