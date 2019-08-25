import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def store(filename, contents):
	with open(filename,"ab") as f:
		f.write(contents)
		f.close()

def read_name():
	files = open("nombres.txt","r")
	lista = files.read()
	lista = lista.split()
	for i in range(len(lista)):
		lista[i] = lista[i].split(',')
	files.close()
	return lista


def store_name(identificador):
	lista = read_name()
	for i in lista:
		if i[0] == identificador [0]:
			if i[1] == identificador[1]:
				pass
			else:
				extra = '1'
				try:
					extra = int(identificador[-5])
					extra += 1
				except:
					identificador[0] = identificador[0][:-4] + extra + identificador[0][-4:]
	print (identificador)
	guardar = ','.join(identificador)
	lista2 = []
	for i in range(len(lista)):
		lista2.append(",".join(lista[i]))
	lista2 = " ".join(lista2)
	lista2 = lista2 + ' ' + guardar	
	files = open("nombres.txt","w")
	files.write(lista2)
	files.close()
	return 1

while True:
	nombre, sha256,contents = socket.recv_multipart() #TODO: Nombre archivo, marca hash, contenido
	identificador = [nombre.decode('utf-8'),sha256.decode()]
	save = store_name(identificador)
	if save == 0:
		socket.send_string('Archivo ya esta en nuestro servidor')
	else:
		store(sha256,contents)
		socket.send_string("chupelo")

print ("Esto no deberia aparecer")


