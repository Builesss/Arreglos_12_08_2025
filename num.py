import numpy as np

vector = np.array([1, 2, 3, 4, 5])
print(vector)

print(vector[2])

""" Los vectores no son como las listas, no tienen un metodo end() para agregar elementos
o tienen un metodo pop() para eliminar elemntos. pero si tienen metodo reshape() para cambiar
su forma, adicionalmente despues de creado no se puede cambiar el tamaño del vector."""

vector1 = np.zeros(5)
print(vector1)

vector2 = np.ones(5)
print(vector2)

vector3 = np.arange(1, 10)
print("rango", vector3)

vector4 = np.linspace(1, 10, 5)
print("linspace", vector4)

vector5 = np.random.rand(10)
print("random", vector5)

vector6 = np.random.randint(1, 10, 10)
print("random int", vector6)