import serial
import pickle
from ds485 import Data


data=Data(123)
data.save("0001",23.4)
data.save("0002",21.5)
data.save("0032",15.5)
data.save("0001",32.9)

data.show()

payload=pickle.dumps(data)
#b=pickle.loads(payload)
#b.show()

ser = serial.Serial(
	port="/dev/ttyUSB0", 
	baudrate=115200, 
	timeout=1,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)  
ser.write(payload)


