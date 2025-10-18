"""
Una calculadora de multplicacion de matrices

El usuario debe ingresar las dimensaiones de la matriz

ejemplo:


xdxdxdxdxdxd

 AXB

'Ingrese numero de filas matriz A: 2'
'Ingrese numero de columnas matriz A: 2'
'Ingrese numero de filas matriz B: 2'
'Ingrese numero de columnas matriz B: 2'

|a00 a01|     |b00 b01|
|a10 a11|  x  |b00 b01|

OJO: el numero de filas y columnas tiene que ser entero
    El numero de filas de la matriz A = El numero de columnas de la matriz B
"""
import numpy as np

print("AxB")

FA = int(input("Ingrese numero de filas matriz A: "))
CA = int(input("Ingrese numero de columnas matriz A: "))
FB = int(input("Ingrese numero de filas matriz B: "))
CB = int(input("Ingrese numero de columnas matriz B: "))

dimensionA = tuple([FA, CA])
dimensionB = tuple([FB, CB])

MA = np.zeros(dimensionA, dtype=object)
MB = np.zeros(dimensionB, dtype=object)

for i in range(FA):
    for j in range(CA):
        MA[i][j] = f"a{i}{j}"

for i in range(FB):
    for j in range(CB):
        MB[i][j] = f"b{i}{j}"

print("")
print(f"{MA}")
print("")
print("X")
print("")
print(f"{MB}")

for i in range(FA):
    for j in range(CA):
        MA[i][j] = float(input(f"Ingrese a{i}{j}: "))

for i in range(FB):
    for j in range(CB):
        MB[i][j] = float(input(f"Ingrese b{i}{j}: "))

def multplyMatrix(MA, MB):
    sol = []

    for i in range(0, len(MA)):
        for j in range(0, len(MB[0])):

            e = 0

            for k in range(0, len(MB)):
                e = MA[i][k]*MB[k][j] + e

            sol.append(e)

    sol = np.array(sol).reshape((len(MA), len(MB[0])))

    return sol

solucion = multplyMatrix(MA, MB)

print("")
print(MA)
print("")
print("X")
print("")
print(MB)
print("")
print("=")
print("")
print(solucion)