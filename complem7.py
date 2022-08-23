import math

print("-------------------------------")
print("TP COMPLEM 7")
print("-------------------------------")


pi = 3.14

print("Ingrese lados del triangulo")
b = float(input("Lado B:"))
c = float(input("Lado C:"))
print("Ingrese el ángulo en grados sexagesimales")
alfa = float(input())


a = (b**2 + c**2 - 2*b*c * math.cos(alfa*pi(180))** 0.50 )

print("El lado es: ", a)