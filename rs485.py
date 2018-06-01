import serial
import pickle

POLLING=1
TEMPERATURES=2

class RS485_payload():
	def __init__(self,source_node,target_node,frame_type):
		self.temperatures={}
		self.source_node=source_node
		self.target_node=target_node
		self.frame_type=frame_type

	def put(self,sensor_id,temp):
		self.temperatures[sensor_id]=temp

	def get(self):
		return self.temperatures

	def get_node_addr(self):
		return self.node_addr

	def __str__(self):
		return str(self.temperatures)	


class RS485():
	def __init__(self,serial_device):
		self.serial_device=serial_device
		self.serial = serial.Serial(
			port=serial_device, 
			baudrate=9600, 
			timeout=1,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)  
		
	def send(self,packet):
		payload=pickle.dumps(packet)
		self.serial.write(payload)
		self.serial.flush()

	def receive(self):
		pass
		