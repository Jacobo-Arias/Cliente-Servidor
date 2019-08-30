'''
Cliente del simulador de Spotify
'''

import zmq
import pygame
import os
pygame.mixer.init()

context = zmq.Context()

def menu(lista):
    while(True):
        a = input('0. Para mostrar lista canciones \nOtro numero para elegir la canción: ')
        try:
            a = int(a)
            if a != 0 and (not lista):
                print('Le recomendamos ver la lista de canciones primero')
            else:
                return a
        except:
            print('No ha digitado un numero')

lista = []
while True:
    op = menu(lista)
    if op == 0:
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")
        socket.send_string('listar')
        contents = socket.recv_json()
        cont = 1
        lista = contents
        for i in range(len(contents)):
            print(str(cont) + '- ' + contents[i])
            cont += 1
        #socket.disconnect("tcp://localhost:5555")
    else:
        socket.send_string(contents[op-1])
        contenido = socket.recv_json()
        for i in contenido:
            socket = context.socket(zmq.REQ)
            socket.connect(i[1])
            socket.send_string(i[0])
            recv = socket.recv()
            filename = open(contents[op-1],'ab')
            filename.write(recv)
            filename.close()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(contents[op-1])
        pygame.mixer.music.play()
        os.system('clear')
        lista =[]

