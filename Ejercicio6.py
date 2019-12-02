def triangular_iterativo(n):
    triangular = 0
    for i in range(1, n+1):
        triangular += i
    return triangular


def triangular_calculado(n):
    return int(n * (n+1)/2)


leyendo = True
while leyendo:
    try:
        n = int(input("Introduzca número de triangulares a calcular: "))
        leyendo = False
    except ValueError:
        print("Introduzca solo valores numéricos enteros\n")

for i in range(1, n+1):
    # print (i,"  -  ",triangularIterativo(i))
    triangular_iterativo(i)


print("Ya")

for i in range(1, n+1):
    print(i, "  -  ", triangular_calculado(i))
    triangular_calculado(i)

print("Otro ya")
