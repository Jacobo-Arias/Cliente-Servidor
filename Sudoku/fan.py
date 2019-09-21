import zmq
import random
import time

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if type(bo[i][j]) is int:
                show = bo[i][j]
            else:
                show = 0 
            if j == 8:
                print(show)
            else:
                print(str(show) + " ", end="")

context = zmq.Context()

# socket with workers
workers = context.socket(zmq.PUSH)
workers.bind("tcp://*:5557")


recvSink = context.socket(zmq.PULL)
recvSink.bind("tcp://*:5559")

board = [
    [0,0,0,7,5,0,0,0,0],
    [0,3,0,0,4,8,0,2,0],
    [1,0,0,0,0,0,0,0,6],
    [0,4,0,0,0,0,0,0,8],
    [7,9,0,0,0,0,0,3,1],
    [2,0,0,0,0,0,0,7,0],
    [5,0,0,0,0,0,0,0,0],
    [0,8,0,3,2,0,0,4,0],
    [0,0,0,0,6,9,0,0,0]
]

def matrizdoble(board):
    doble = []
    for i in board:
        aux = []
        for j in i:
            if j == 0:
                aux.append([])
            else:
                aux.append(j)
        doble.append(aux) 
    return doble

matrizsub = matrizdoble(board)
listwork = [matrizsub]

print("Press enter when workers are ready...")
_ = input()
print("sending tasks to workers")

totalTime = 0
while True:
    for work in range(len(listwork)):
        workers.send_json(listwork.pop(1))
    recivido = recvSink.recv_string()
    if type(recivido) is list:
        listwork += recivido
    elif type(recivido) is dict:
        print_board(recivido['solution'])
        break
