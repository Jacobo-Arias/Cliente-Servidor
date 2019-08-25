import zmq
import os
import hashlib

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

filename = "namefile.txt"

with open(filename,"rb") as filef:
    hash_archivo = hashlib.sha256()  
    while True: 
        contents = filef.read(10*1024*1024)
        if not contents:
            break
        hash_archivo.update(contents) 
    filef.close() 
            
sha_file = hash_archivo.hexdigest().encode()

with open(filename,"rb") as f:
    while(True):
        contents = f.read(10*1024*1024)
        if not contents:
            break
        else:
            socket.send_multipart([filename.encode("utf-8"),sha_file,contents]) #TODO: Nombre archivo, marca hash, contenido
            m = socket.recv_string()
    f.close()
print("Recibi: {}".format(m))
