import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.17.27:5555")


filename = "jacobo1g.txt"
with open(filename,"rb") as f:
    contents = f.read(10*1024*1024)
    socket.send_multipart([filename.encode("utf-8"),contents])
m = socket.recv_string()
print("Recibi: {}".format(m))
