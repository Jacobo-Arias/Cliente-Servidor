import sys
import time
import zmq

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

fan = context.socket(zmq.PULL)
fan.bind("tcp://*:5558")

sendFan = context.socket(zmq.PUSH)
sendFan.connect("tcp://localhost:5559")


# Start our clock now
tstart = time.time()

# Process 100 confirmations
while True:
    listwork = fan.recv_json()
    if type(listwork) is list:
        sendFan.send_json(listwork)
    elif type(listwork) is dict:
        sendFan.send_json(listwork)
        print_board(listwork['solution'])
        break
