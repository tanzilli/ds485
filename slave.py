import serial
import pickle
import time
from ds485 import Data		

ser = serial.Serial(
	port="/dev/ttyUSB1", 
	baudrate=115200, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  

while True:
	a=ser.in_waiting
	print a
	if a>0:
		payload=ser.read(a)
		print payload
		b=pickle.loads(payload)
		print b.get_data()
		print b.get_address()
	time.sleep(2)
