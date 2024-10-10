while True:
    try:
        n1 = int(input("Escribe un entero: "))
        n2 = int(input("Escribe otro entero: "))
    except ValueError:
        print("Tienes que escribir un número entero")

n3 = n1+n2

print("La suma de ambos números es",n3,".")