
name = str(input("Hola, quin es el teu nom? "))
edat = int(-1)

# Preguntamos la edad e indicamos si es mayor o menor de edad.
while edat <= 0:
    edat = int(input("Quina edat tens? "))
    if edat >= 18:
        print('Hola ' + name + ', ets major de edat')
        break
    else:
        if edat > 0:
            print('Hola ' + name + ', ets menor de edat')
            break
    print("Tu edad debe ser un número mayor a 0.")

print("Programa finalitzat")
