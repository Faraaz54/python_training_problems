from math import sqrt
def factorial(n):
    """Computes factorial of n."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
    factor = (sqrt(2) * 2) / 9801
    k = 0
    total = 0
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = (factorial(k)**4) * (396**(4*k))
        term = factor * num / den
        total += term
        if abs(term) < 1e-15:
            break
        k = k + 1

    return 1 / total


pi = estimate_pi()
print pi
