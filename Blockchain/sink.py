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

# Process 100 confirmations
diccionario = fan.recv_json()
print('Para la cadena \'',s,'\':')
print('El usuario que primero lo encontro fue ',diccionario['Usuario'],'\n\nEl hash encontrado fue: ',diccionario['Hash'],
'\n\nEn ', diccionario['intentos'],' intentos', '\n\nY la respuesta fue: ',diccionario['Respuesta'])

# Calculate and report duration of batch
tend = time.time()
print("Total elapsed time: %d msec" % ((tend-tstart)*1000))
