from io import open

fichero = open ('persona.txt','r',encoding="utf8")

lista = []


for p in fichero:
	
	q = p.split(';')

	if q[3][-1:] == "\n":
	
		q[3] = q[3][:-1]
	
	usuario = {'id':q[0],'nombre':q[1],'apellido':q[2],'nacimiento':q[3]}
	lista.append(usuario)

for l in lista:
	print ('ID: {}\tUsuario: {}\t{}\t\tNacimiento: {}'.format(l['id'],l['nombre'],l['apellido'],l['nacimiento']))

fichero.close()
