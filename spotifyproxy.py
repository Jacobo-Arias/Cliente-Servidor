'''
Proxy del simulador de Spotify
'''
import zmq

context = zmq.Context()

socket_recv = context.socket(zmq.REP)
socket_recv.bind("tcp://*:5555")

servidores = ["tcp://localhost:5554","tcp://localhost:5553","tcp://localhost:5552"]

def listar(objeto = 'Deja Vu.mp3'):
    contenido = {}
    for j in range(len(servidores)):
        socket = context.socket(zmq.REQ)
        socket.connect(servidores[j])
        socket.send_string(objeto)
        contents = socket.recv_json()
        for i in range(len(contents)):
            nombre = contents[i]
            contents[i] = contents[i].split('#%#&')
            contents[i][0] = contents[i][0].split('-')
            if contents[i][1] not in contenido:
                aux = list(range(int(contents[i][0][1])))
                contenido[contents[i][1]] = aux
            contenido[contents[i][1]][int(contents[i][0][0])-1] = [nombre,servidores[j]]
    return contenido

canciones = listar('listar')

while True:
    reciv = socket_recv.recv_string()
    if reciv == 'listar':
        retorno = []
        for key in canciones:
            retorno.append(key)
        socket_recv.send_json(retorno)
    else:
        socket_recv.send_json(canciones[reciv])
'''
#print(canciones)
retorno = []
for key in canciones:
    retorno.append(key)
print(retorno)'''
