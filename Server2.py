import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def store(message, filename):
	with open(filename,"a") as f:
		f.write(message)


while True:
	names1,sha256,contents = socket.recv_multipart()
	store(m,"f-" + str(names1.decode("utf-8")))
	socket.send_string("chupelo")

print ("Esto no deberia aparecer")



'''
files = open("ejemplo.txt","r")
lista = files.read()
lista = lista.split()
for i in range(len(lista)):
    lista[i] = lista[i].split(',')
print (lista)
files.close()


lista2 = []
for i in range(len(lista)):
    lista2.append(",".join(lista[i]))
lista2 = " ".join(lista2)
print(lista2)
files = open("ejemplo2.txt","w")
files.write(lista2)
'''
