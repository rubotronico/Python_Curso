from io import open 
import sys

if len(sys.argv) == 1:
	try:
		fichero = open ('contador.txt','r',encoding='utf8')
		contador = fichero.read()
		fichero.close()
		
		
	except:
		fichero = open ('contador.txt', 'w',encoding='utf8')
		contador = '0'
		fichero.write(contador)
		fichero.close()
		
else:
	if sys.argv[1] == 'inc':
		print ('inc')
		fichero = open ('contador.txt', 'r+', encoding='utf8')
		contador = int(fichero.read())
		contador = str(contador+1)
		fichero.seek(0)
		fichero.writelines(contador)
		fichero.close()

	elif sys.argv[1] == 'dec':
		print ('dec')
		fichero = open ('contador.txt', 'r+', encoding='utf8')
		contador = int(fichero.read())
		contador = str(contador-1)
		fichero.seek(0)
		fichero.writelines(contador)
		fichero.close()

	else:
		fichero = open('contador.txt', 'r', encoding='utf8')
		contador = fichero.read()
		fichero.close()
print(contador)