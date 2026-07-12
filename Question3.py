import numpy as np
import math

def f(x):
    return np.exp(x**2)

a = 0
b = 1

n = 100


def trapezoidal(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a, b, n+1)

    result = h * (0.5*f(x[0]) +
                  sum(f(x[1:-1])) +
                  0.5*f(x[-1]))

    return result


def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1

    h = (b-a)/n
    x = np.linspace(a, b, n+1)

    result = h/3 * (f(x[0]) + f(x[-1]) +
                    4*sum(f(x[1:-1:2])) +
                    2*sum(f(x[2:-1:2])))

    return result


trap_result = trapezoidal(f, a, b, n)
simp_result = simpson(f, a, b, n)


print("Trapezoidal result:", trap_result)
print("Simpson result:", simp_result)
from scipy.integrate import quad

gauss_result, error = quad(f, 0, 1)

print("Gaussian result:", gauss_result)
