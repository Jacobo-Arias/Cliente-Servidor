import sys
import time
import zmq

context = zmq.Context()

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def filtrar(matrizsub):
    for fil in range(len(matrizsub)):
        for col in range(len(matrizsub)):
            for num in range(1,10):
                if valid(matrizsub,num,(fil,col)) and type(matrizsub[fil][col]) is list:
                    matrizsub[fil][col].append(num)
    return matrizsub

def fillone(matrizsub):
    cambio = False
    for fil in range(len(matrizsub)):
        for col in range(len(matrizsub)):
            if type(matrizsub[fil][col]) is list:
                if len(matrizsub[fil][col]) == 1:
                    matrizsub[fil][col] = matrizsub[fil][col].pop()
                    cambio = True

    return matrizsub,cambio

def reset(matrizsub):
    for fil in range(len(matrizsub)):
        for col in range(len(matrizsub)):
            if type(matrizsub[fil][col]) is list:
                matrizsub[fil][col] = []
    return matrizsub

def work(matrizsub):
    matrizsub = reset(matrizsub)
    matrizsub= filtrar(matrizsub)
    matrizsub,cambio = fillone(matrizsub)
    return matrizsub,cambio


work = context.socket(zmq.PULL)
work.connect("tcp://localhost:5557")

# Socket to send messages to
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

# Process tasks forever
while True:
    w2d = work.recv_json()
    listwork = [w2d]
    for iteraciones in range(10):
        w2d = listwork.pop(0)
        cambio = True
        while cambio:
            w2d,cambio = work(w2d)
        
        # listwork.append()
        menosOP = 9
        xy = []
        for fil in range(len(w2d)):
            for col in range(len(w2d)):
                if type(w2d[fil][col]) is list:
                    if len(w2d[fil][col]) < menosOP:
                        menosOP = len(w2d[fil][col])
                        xy = [fil,col]

        candidato = w2d
        for i in range(menosOP):
            candidato[xy[0]][xy[1]]=w2d[xy[0]][xy[1]][i]
            listwork.append(candidato)

    # Send results to sink
    sink.send_json(listwork)
