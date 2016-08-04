import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5610")

id = 0
ite = 0
while ite < 10:
    time.sleep(1)
    id += 1
    
    # Message [prefix][message]
    message = "1-Message #{id} ".format(id=id)
    sock.send(message)

    # Message [prefix][message]
    message = "2-Message #{id} ".format(id=id)
    sock.send(message)

    ite += 1
    print "Sent: {msg}".format(msg=message)

