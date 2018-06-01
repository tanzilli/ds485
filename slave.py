import pickle
import time
from rs485 import RS485	
from rs485 import RS485_payload
import rs485

while True:
	a=ser.in_waiting
	if a>0:
		print "Bytes received %d" %a	
		payload=ser.read(a)
		print payload
		try:
			b=pickle.loads(payload)
			print b
	#		print b.get_node_addr()
		except:
			pass
