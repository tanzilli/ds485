import serial
import pickle
import time
from ds485 import DS485_data		

ser = serial.Serial(
	port="/dev/ttyUSB1", 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  

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
