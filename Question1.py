import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline
x = np.array([1,2,3,4,5,6])
y = np.array([1,3,5,8,5,2])
poly = lagrange(x, y)

print("Polynomial:")
print(poly)
spline = CubicSpline(x, y)
xx = np.linspace(1, 6, 200)

plt.figure(figsize=(8,5))

plt.scatter(x, y, color="red", label="Data Points")

plt.plot(xx, poly(xx), label="Lagrange")

plt.plot(xx, spline(xx), label="Cubic Spline")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange and Cubic Spline Interpolation")

plt.grid(True)
plt.legend()

plt.show()
print("Spline(2.5) =", spline(2.5))
print("Spline(4.5) =", spline(4.5))
