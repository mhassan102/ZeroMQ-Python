import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:5600")

time.sleep(15)

while True:
    print "Next Pop"
    message = sock.recv()
    print "Received: {msg}".format(msg=message)
