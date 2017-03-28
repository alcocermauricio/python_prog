print("Ingresa 3 numeros para sacarle la media\n")

suma1 = float(input("Ingrese el primer Numero: "))
suma2 = float(input("Ingrese el segundo Numero: "))
suma3 = float(input("Ingresa el Ultimo Numero: "))

def media (a, b, c):
	media=(a + b + c)/3
	print("La media de ", a," ", b, "  ", c, " es ", media)
	return
media(suma1, suma2, suma3)

input()
