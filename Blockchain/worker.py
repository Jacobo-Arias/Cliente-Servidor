import sys
import time
import zmq
import random
import hashlib
import string

context = zmq.Context()

work = context.socket(zmq.PULL)
work.connect("tcp://localhost:5557")

# Socket to send messages to
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

def hashString(s):
    sha = hashlib.sha256()
    sha.update(s.encode('ascii'))
    return sha.hexdigest()

def generation(challenge, size = 25):
    answer = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
                      for x in range(size))
    attempt = challenge + answer
    return attempt, answer

def proofOfWork(challenge):
    found = False
    attempts = 0
    while not found:
        attempt, answer = generation(challenge, 64)
        #print(attempt)
        hash = hashString(attempt)
        if hash.startswith('0000'):
            found = True
            #print(hash)
        attempts += 1
    print(attempts)
    return hash,attempts,answer


user= input("Diga su nombre: ")
# Process tasks forever
while True:
    s = work.recv_string()
    challenge = hashString(s)
    hash, attempts, answer = proofOfWork(challenge)
    print('finish, sent')
    enviar = {'Usuario':user,'Hash':hash,'intentos':attempts,'Respuesta':answer}

    # Send results to sink
    sink.send_json(enviar)