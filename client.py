import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.17.27:5555")

socket.send_string("Jacobo Arias")
m = socket.recv()
print("Recibi: {}".format(m))
