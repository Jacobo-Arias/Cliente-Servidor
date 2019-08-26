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

archivos = ls()

while True:
    nombre = socket.recv_string()
    if nombre != 'listar':
        try:
            mensaje = open(nombre,'rb')
            contents = mensaje.read()
            socket.send_multipart([contents,nombre.encode('utf-8')])
            mensaje.close()
        except:
            socket.send_multipart(['0'.encode('utf-8'),'0'.encode('utf-8')])
    else:
        socket.send_json(archivos)


print ("Esto no deberia aparecer")