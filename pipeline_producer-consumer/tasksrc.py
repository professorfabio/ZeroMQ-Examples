import multiprocessing
import zmq, time, pickle, sys, random
from constPipe import * #-

def producer(port):
	context = zmq.Context()              
	socket  = context.socket(zmq.PUSH)        # create a push socket
	socket.bind("tcp://localhost:"+port)                             # bind socket to address
	
	for i in range(100):                  # generate 100 workloads
		workload = random.randint(1, 100)   # compute workload
		socket.send(pickle.dumps(workload)) # send workload to worker

if sys.argv[1] == '1':
	producer(PORT1)
elif sys.argv[1] == '2':
	producer(PORT2)
