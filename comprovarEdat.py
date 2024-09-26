name = str(input("Hola, quin es el teu nom? "))
edat = int(1)

while edat != 0:
    edat = int(input("Quina edat tens? "))
    if edat >= 18:
    print('Hola ' + name + ', ets major de edat')
    else:
    print('Hola ' + name + ', ets menor de edat')


# Finalizamos programa
print("Programa finalitzat")

