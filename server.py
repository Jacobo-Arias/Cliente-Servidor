import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    m = socket.recv()
    print("Mensaje recibido {}".format(m))
    socket.send_string("chupelo")

print ("Esto no deberia aparecer")
