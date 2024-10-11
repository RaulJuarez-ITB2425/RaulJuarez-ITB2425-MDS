print('Escribe dos enteros para dividirlos.')
while True:
    try:
        n1 = int(input("Escribe un entero (el dividendo): "))
        n2 = int(input("Escribe otro entero (el divisor): "))
        break
    except ValueError:
        print("Tienes que escribir números enteros")

n3=float(n1/n2)
n3=str(n3)

print('El resultado de la división es: '+n3)