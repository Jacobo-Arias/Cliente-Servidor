'''
Cliente del simulador de Spotify
'''

import zmq
import pygame
import os
pygame.mixer.init()

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

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
        socket.send_string('listar')
        contents = socket.recv_json()
        cont = 1
        lista = contents[1:]
        for i in range(len(lista)):
            print(str(cont) + '- ' + lista[i])
            cont += 1
    else:
        socket.send_string(contents[op])
        contents,nombre = socket.recv_multipart()    
        nombre = nombre.decode('utf-8')
        filename = open(nombre,'wb')
        filename.write(contents)
        filename.close()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(nombre)
        pygame.mixer.music.play()
        os.system('clear')
        lista =[]

