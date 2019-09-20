import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server…")
socket.connect("tcp://localhost:5556")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001" #coloco el primer valor que me pasaron por linea de comandos, si no pasan nada paso 10001

# Python 2 - ascii bytes to unicode str
if isinstance(zip_filter, bytes): #si zip_filter está en bytes
    zip_filter = zip_filter.decode('ascii')

socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter) #dice que solo esta interesado en ciertos datos que manda, en este caso es zip_filter 

# Process 5 updates
total_temp = 0
for update_nbr in range(5):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

print("Average temperature for zipcode '%s' was %dF" % (
      zip_filter, total_temp / (update_nbr+1))
)