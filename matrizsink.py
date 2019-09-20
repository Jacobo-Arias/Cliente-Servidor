import sys
import time
import zmq

context = zmq.Context()

fan = context.socket(zmq.PULL)
fan.bind("tcp://*:5558")

# Wait for start of batch
s = fan.recv_string()

# Start our clock now
tstart = time.time()

s = int(s)
ss = math.sqrt(s)


R = [[0,0,0], [0,0,0], [0,0,0]]
print(R)
for task in range(s):
    s = fan.recv_json()
    R[s["i"]][s["j"]] = s["result"]


print (R)
# Calculate and report duration of batch
tend = time.time()
print("Total elapsed time: %d msec" % ((tend-tstart)*1000))