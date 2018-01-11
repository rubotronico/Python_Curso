import sys
if len(sys.argv) == 3:
	f = int(sys.argv[1])
	c = int(sys.argv[2])
	if f<1 or f>9 or c<1 or c>9:
		print ("Error: Filas o Columna incorrectas")
		print ("Ejemplo: python tabla.py filas[1-9] columnas[1-9]")
	else:
		for n in range(f):
			for m in range(c):
				print(" * ", end='')
			print()
			
else:
	print ("Error")
	print ("Ejemplo: python tabla.py filas columnas")