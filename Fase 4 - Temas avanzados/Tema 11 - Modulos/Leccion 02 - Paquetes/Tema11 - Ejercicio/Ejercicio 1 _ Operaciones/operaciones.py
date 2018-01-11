def suma():
	print ("Operacion Suma")
	try:
		n = float(input("\tIntroduce un número: "))
		m = float(input("\tIntroduce un número: "))
		print("\t{} + {} = {}".format(n , m , n+m))
	except TypeError:
		print ("Ha ocurrido un error, introduce un número válido.")
	except ValueError:
		print ("Ha ocurrido un error, introduce un número válido.")

def resta():
	print ("Operacion Resta")
	try:
		n = float(input("\tIntroduce un número: "))
		m = float(input("\tIntroduce un número: "))
		print("\t{} - {} = {}".format(n , m , n-m))
	except TypeError:
		print ("Ha ocurrido un error, introduce un número válido.")
	except ValueError:
		print ("Ha ocurrido un error, introduce un número válido.")


def producto():
	print ("Operacion Producto")
	try:
		n = float(input("\tIntroduce un número: "))
		m = float(input("\tIntroduce un número: "))
		print("\t{} x {} = {}".format(n , m , n*m))
	except TypeError:
		print ("Ha ocurrido un error, introduce un número válido.")
	except ValueError:
		print ("Ha ocurrido un error, introduce un número válido.")

def division():
	print ("Operacion División")
	try:
		n = float(input("\tIntroduce un número: "))
		m = float(input("\tIntroduce un número: "))
		print("\t{} / {} = {}".format(n , m , n/m))
	except TypeError:
		print ("Ha ocurrido un error, introduce un número válido.")
	except ZeroDivisionError:
		print ("No se puede dividir entre cero, prueba otro número.")
	except ValueError:
		print ("Ha ocurrido un error, introduce un número válido.")