import zmq
import os
from os import listdir
from os.path import isfile, join


def ls(ruta = '.'):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]

archivos = ls('Canciones')

for filename in archivos:
    sizefile = os.stat('Canciones/' + filename).st_size
    num_partes = int(sizefile/2000000) + 1
    with open('Canciones/' + filename,"rb") as filef:
        contador = 1
        while True: 
            contents = filef.read(2*1024*1024)
            if not contents:
                break
            file2 = 'PartesCanciones/' + str(contador) + '-' + str(num_partes) + '#%#&' + filename        
            f2 = open(file2,'wb')
            f2.write(contents)
            f2.close() 
            contador += 1
filef.close() 