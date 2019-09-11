import zmq
import random
import time

context = zmq.Context()

# socket with workers
workers = context.socket(zmq.PUSH)
workers.bind("tcp://*:5557")

# socket with sink
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")


print("Press enter when workers are ready...")
n = input('Numero de esclavos: ')
print("sending tasks to workers")

cadena = 'Jacobo'

sink.send_string(cadena)
for i in range(int(n)):
    workers.send_string(cadena)

print("Work sent")
while True:
    pass
