from io import open

texto = "Una línea con texto\nOtra línea con texto"
fichero = open('prueba_rubencin.txt','w')
fichero.write(texto)
fichero.close()
fichero = open('prueba_rubencin.txt','r')
texto = fichero.read()
fichero.close()
print (texto)
texto = texto + '\nOtra línea más con texto'
print (texto)
fichero = open ('prueba_rubencin.txt','a')
fichero.write('\nOtra fuckin línea más...')
fichero.close()
print (texto)
with open ('prueba_rubencin.txt','r') as fichero:
	for linea in fichero:
		print (linea)