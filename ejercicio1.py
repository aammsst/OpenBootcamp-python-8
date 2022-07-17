# Primer intento - Mal interpreté la consigna, pero quedó interesante igual
# 
## Creamos archivo py ( ejercicio11 )
#f = open('ejercicio11.py','w')
## Creamos archivo de texto ( texto1 ) y escribimos en él
#f.write('f = open(\'texto1.txt\',\'w\')\nf.write(\'Hola xd\')\nf.close()')
#
#f.close()
## Importamos ejercicio11 para que se ejecute lo que escribimos antes 
#import ejercicio11

# Segundo intento después de ver la resolución
file = open('archivoTxt.txt', 'w')
file.write('Hola!\n')
file.close()

file = open('archivoTxt.txt', 'r+')
file.readline()
file.write('Segunda vez escribiendo.')
file.close()
