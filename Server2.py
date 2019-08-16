import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def store(message, filename):
	with open(filename,"wb") as f:
		f.write(message)


while True:
	name,m = socket.recv_multipart()
	store(m,"f-" + str(name.decode("utf-8")))
	socket.send_string("chupelo")

print ("Esto no deberia aparecer")
