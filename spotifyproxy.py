'''
Proxy del simulador de Spotify
'''
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5554")

socket_recv = context.socket(zmq.REP)
socket_recv.bind("tcp://*:5555")

def pedir(objeto = 'Deja Vu.mp3'):
    if objeto == 'listar':
        socket.send_string(objeto)
        contents = socket.recv_json()
        return contents

    else:
        socket.send_string(objeto)
        contents,nombre = socket.recv_multipart()
        nombre = nombre.decode('utf-8')
        if nombre == '0':
            print('esto no deberia salir')
            pass
        else:
            '''filename = open(nombre,'wb')
            filename.write(contents)
            filename.close()'''
            return contents

def mandar():
    cancion = socket_recv.recv_string()
    contents = pedir(cancion)
    if cancion == 'listar':
        socket_recv.send_json(contents)
    else:
        socket_recv.send_multipart([contents,cancion.encode('utf-8')])
    pass

while True:
    mandar()