import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

suma = vector1 + vector2
print("\033[31mSuma de vectores:", suma, "\033[0m")

producto = vector1 * vector2
print("\033[32mProducto de vectores:", producto, "\033[0m")

division = vector1 / vector2
print("\033[33mDivision de vectores:", division, "\033[0m")

resta = vector1 - vector2
print("\033[34mResta de vectores:", resta, "\033[0m")

potencia = vector1 ** 2
print("\033[35mPotencia de vectores:", potencia, "\033[0m")