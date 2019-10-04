import sys
import time
import zmq

context = zmq.Context()

fan = context.socket(zmq.PULL)
fan.bind("tcp://*:5558")

sendFan = context.socket(zmq.PUSH)
sendFan.connect("tcp://localhost:5559")

# Wait for start of batch
s = fan.recv_string()

# Start our clock now
tstart = time.time()

# Process 100 confirmations
while True:
    for task in range(int(s)):
        #print(task)
        recvwork = fan.recv()
        if task % 10 == 0:
            sys.stdout.write(':')
        else:
            sys.stdout.write('.')
        sys.stdout.flush()
        print("-")
    print('llegaron todas')
    sendFan.send_string('Next')

# Calculate and report duration of batch
tend = time.time()
print("Total elapsed time: %d msec" % ((tend-tstart)*1000))
