import serial
import pickle

class DS485_data():
	def __init__(self,source_node,dest_node):
		self.temperatures={}
		self.source_node=source_node
		self.dest_node=dest_node

	def put(self,sensor_id,temp):
		self.temperatures[sensor_id]=temp

	def get(self):
		return self.temperatures

	def get_node_addr(self):
		return self.node_addr

	def __str__(self):
		return str(self.temperatures)	


class RS485():
	def __init__(self,node_addr,serial_device):
		self.node_addr=node_addr

		self.serial_out = serial.Serial(
			port=serial_device, 
			baudrate=9600, 
			timeout=1,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)  
		
		def send(self,ds485_data):
			payload=pickle.dumps(data)
			self.serial.write(payload)
			self.serial.flush()

		def receive(self):
			pass
		