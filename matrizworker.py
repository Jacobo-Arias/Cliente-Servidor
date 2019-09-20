import sys
import time
import zmq

context = zmq.Context()

work = context.socket(zmq.PULL)
work.connect("tcp://192.168.17.27:5557")

# Socket to send messages to
sink = context.socket(zmq.PUSH)
sink.connect("tcp://192.168.17.27:5558")

# Process tasks forever
while True:
    s = work.recv()
    print(s)
    dot = 0
    X = s["x"]
    Y = s["y"]
    for (i,j) in zip (X,Y)
        dot += i*j
    
    # Send results to sink
    sink.send_json({"result":dot, "i":s["i"], "j":s["j"]})