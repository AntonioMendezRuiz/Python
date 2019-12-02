def interes_compuesto(ci, x, n):
    return ci * (1 + x / 100) ** n


leyendo = True
while leyendo:
    try:
        capital_inicial = float(input("Introduce el capital inicial: "))
        anios = float(input("Introduce los años  : "))
        interes = float(input("Introduce el interés (%): "))
        leyendo = False
    except ValueError:
        print("Error en la introducción de datos\n")

print("Total a pagar: ", interes_compuesto(
    capital_inicial, interes, anios), "euros")

