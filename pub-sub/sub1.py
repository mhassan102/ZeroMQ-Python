import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)

time.sleep(15)

# Define subscription and messages with prefix to accept.
sock.setsockopt(zmq.SUBSCRIBE, "1")
sock.connect("tcp://127.0.0.1:5610")

while True:
    print "Next Pop"
    message = sock.recv()
    print "Received: {msg}".format(msg=message)
