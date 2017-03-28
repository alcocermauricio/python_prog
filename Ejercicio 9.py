import math
i = float(input("ingrese el cateto: \n"))
o = float(input("ingrese el siguiente cateto: \n"))

def hipotenusa (i, o):
	Hp = math.sqrt(( i*i + o*o))
	print("La hipotenusa de triangulo rectangulo es :")
	print(Hp)
	
hipotenusa(i, o)

input()

