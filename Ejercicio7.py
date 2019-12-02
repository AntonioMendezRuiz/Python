leyendo = True
while leyendo:
    try:
        m = int(input("Introduzca número factoriales a calcular: "))
        leyendo = False
    except ValueError:
        print("Introduzca solo valores numéricos enteros\n")

for i in range(1, m+1):
    leyendo = True
    while leyendo:
        try:
            n = 8
            int(input("Introduzca un número para calcular su factorial: "))
            leyendo = False
        except ValueError:
            print("Introduzca solo valores numéricos enteros\n")
    factorial = 1
    for j in range(2, n+1):
        factorial *= j
    print(i, n, factorial)
