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

recvSink = context.socket(zmq.PULL)
recvSink.bind("tcp://*:5559")

totalwait = input('Tareas totales: ')
totalwait = int(totalwait)
timewait = input('Tareas por lote: ')
sink.send_string(timewait)
timewait = int(timewait)

print("Press enter when workers are ready...")
_ = input()
print("sending tasks to workers")


random.seed()

totalTime = 0
while totalwait > 0:
    for task in range(timewait):
        workload = random.randint(1,100)
        totalTime += workload
        workers.send_string(u'%i' % workload)
    totalwait -= timewait
    nxt = recvSink.recv_string()

print("Total expected cost: %s msec" % totalTime)
while True:
    pass
