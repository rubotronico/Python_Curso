import sys

if len(sys.argv) == 2:
	numero = int (sys.argv [1])
	if numero < 0:
		print ("Error: introducir un número positivo entero")
	else:
		n = str(numero)
		l = len(n)
		for i in range (l):
			print("{:05d}".format(int(n[l-1-i])* 10 ** i))
else:
	print ("Error: introducir solo un argumento.")
	print ("Ejemplo: python descoposicion.py 3")

	



