'''
Servidor del simulador de Spotify
'''

import zmq
import os
from os import listdir
from os.path import isfile, join

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")


def ls(ruta = '.'):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]

archivos = ls('Canciones')

while True:
    nombre = socket.recv_string()
    if nombre != 'listar':
        mensaje = open('Canciones/' + nombre,'rb')
        contents = mensaje.read()
        socket.send(contents)
        mensaje.close()
    else:
        socket.send_json(archivos)


print ("Esto no deberia aparecer")