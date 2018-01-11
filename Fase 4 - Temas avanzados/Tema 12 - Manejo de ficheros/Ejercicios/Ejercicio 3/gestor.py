import pickle
from io import open


class Personaje():
	def __init__(self, clase, vida, ataque, defensa, alcance):
		self.clase = clase
		self.vida = vida
		self.ataque = ataque
		self.defensa = defensa
		self.alcance = alcance
		personaje = {'clase': self.clase, 'vida': self.vida, 'ataque': self.ataque, 'defensa': self.defensa, 'alcance': self.alcance}
		print ('Se ha creado el personaje: {}'.format (self.clase))
		print (personaje)

class Gestor():

	lista = []

	def __init__(self):
		self.cargar()

	def añadir(self,p):
		self.lista.append(p)
		print ('Se ha añadido el {}.'.format(p.clase))
		self.guardar()

	def mostrar(self):
		if len(self.lista) == 0:
			print('No hay personajes.')
			return
		for p in self.lista:
			print ('{:15}L:{} A:{} D:{} R:{}'.format(p.clase, p.vida, p.ataque, p.defensa, p.alcance))

	def eliminar(self,clase):
		for l in self.lista:
			if clase == l.clase:
				g.lista.remove(p)
		self.guardar()

	def cargar(self):
		fichero = open('personajes.pckl', 'ab+')
		fichero.seek(0)
		try:
			self.personajes = pickle.load(fichero)
		except:
			print ('El fichero personajes.pckl está vacío.')
		finally:
			fichero.close
			print('Se han cargado {} personajes'.format(len(self.lista)))

	def guardar(self):
		fichero = open('personajes.pckl', 'wb')
		pickle.dump(self.lista, fichero)
		fichero.close()
		

	
g = Gestor()
p = Personaje('Caballero',4,2,4,2)
g.añadir(p)
p = Personaje('Guerrero',2,4,2,4)
g.añadir(p)
p = Personaje('Arquero',2,4,1,8)
g.añadir(p)
g.mostrar()
g.eliminar('Arquero')
g.mostrar()