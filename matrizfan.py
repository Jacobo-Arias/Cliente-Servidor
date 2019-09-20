import zmq
import random
import time

context = zmq.Context()

#socket with workers
workers = context.socket(zmq.PUSH)
workers.bing("tcp://*:5557")

#socket with sink
sink = context.socket(zmq.PUSh)
sink.connect("tcp://localhost:5558")

X = [[12,7,3],
     [4,5,6],
     [7,8,9]]

Y = [[5,8,1],
     [4,5,6],
     [4,5,9]]
    
print("Press enter when worlers are ready...")
_ = input()
print("Sending tasks to workers")

numtask = len(X) * len(Y[0])
sink.send_string(u'%i'% numtask)

print("Task to be sent {}".format(numtask))
for i in range(len(X[0])):
    for j in range(len(Y)):
        w = json.dumps({"x":X[i],'y':Y[j],'i':i,'j':j})
        workers.send_string(w)

print("Done!!!")
while True:
    pass
