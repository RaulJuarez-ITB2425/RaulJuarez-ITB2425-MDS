import math

n1 = float(input("Escribe un número: "))
#En python el uso de round() redondea hacia el par más cercano cuando ponemos un decimal a la mitad (5).
#n1=round(n1)

#Usando math.ceil() el redondeo funciona como usualmente. Para usarlo debemos haber importado math.
n1=math.ceil(n1)

print(n1)