print("-------------------------")
print("TP COMPLEM 10")
print("-------------------------")


print("Ingrese valores del A(x1, y1 y z1):")
x1 = float(input())
y1 = float(input())
z1 = float(input())

print("Ingrese valores del A(x2, y2 y z2):")
x2 = float(input())
y2 = float(input())
z2 = float(input())

dis = ( (z2-z1)**2 + (y2-y1)**2 + (x2-x1)**2)**0.5

print("La distancia es: ", dis)
