import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PUSH)
sock.bind("tcp://127.0.0.1:5600")

id = 0
ite = 0
while ite < 10:
    id += 1
    
    # Message [id] - [message]
    message = "1-Message #{id} ".format(id=id)
    sock.send(message)

    ite += 1
    print "Sent: {msg}".format(msg=message)
