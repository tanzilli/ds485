import serial
import pickle
import time
from ds485 import DS485_data	

#temperatures={'1111': 15.5, '2222': 32.9, '0001': 18.4, '0002': 21.5}


data=DS485_data(100)
data.put("0001",18.4)
data.put("0002",21.5)
data.put("1111",15.5)
data.put("2222",32.9)

print "\nPRIMA"
print data

payload=pickle.dumps(data)
print "\nPAYLOAD"
print payload

# Deserializza la classe
out_data=pickle.loads(payload)

print "\nDOPO"
print out_data

serial_out = serial.Serial(
	port="/dev/ttyUSB0", 
	baudrate=9600, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  

print len(payload)
serial_out.write(payload)
serial_out.flush()
time.sleep(10)
serial_out.close()




