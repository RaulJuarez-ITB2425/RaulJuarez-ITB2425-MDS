valor1 = ''
valor2 = ''
while valor1 not in ('T', 'F') or valor2 not in ('T', 'F'):
    valor1 = str(input("Escribe T o F para el valor 1: ").upper())
    valor2 = str(input("Escribe T o F para el valor 2: ").upper())
    print("")

if valor1=='T':
    valor1 = bool(True)
else:
    if valor1 == 'F':
        valor1 = bool(False)

if valor2=='T':
    valor2 = bool(True)
else:
    if valor2 == 'F':
        valor2 = bool(False)

and_result = valor1 and valor2
or_result = valor1 or valor2
not_valor1 = not valor1
not_valor2 = not valor2

print("Finalizamos programa")