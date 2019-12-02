def fahrenheit_celsius(f):
    return (f - 32)*5/9


leyendo = True
while leyendo:
    try:
        faren = float(input("Introduzca temperatura en grados Fahrenheit: "))
        leyendo = False
    except ValueError:
        print("Introduzca un valor numérico\n")


print("La temperatura equivalente en grados centígrados es :",
      fahrenheit_celsius(faren))
