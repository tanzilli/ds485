import serial
import pickle

TEMP=2
RELAY=3

class Packet():
	def __init__(self,target_node,frame_type=TEMP):
		self.sensors={}
		self.target_node=target_node
		self.frame_type=frame_type
		self.relay_state=0

	def put(self,sensors):
		self.sensors=sensors

	def get(self):
		return self.sensors

	def get_target_node(self):
		return self.target_node

	def get_frame_type(self):
		return self.frame_type

	def set_relay_state(self,state):
		self.relay_state=state

	def get_relay_state(self):
		return self.relay_state

	def __str__(self):
		return str(self.sensors)	

class Link():
	def __init__(self,serial_device):
		self.error_counter=0
		self.message_counter=0
		self.serial_device=serial_device
		self.serial = serial.Serial(
			port=serial_device, 
			baudrate=115200, 
			timeout=0.2,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)  

	def get_message_counter(self):
		return self.message_counter

	def get_error_counter(self):
		return self.error_counter
		
	def send(self,packet):
		payload=pickle.dumps(packet)
		self.serial.reset_output_buffer()
		self.serial.write(payload)
		self.serial.flush()

	def receive(self):
		self.serial.reset_input_buffer()
		while True:
			rx_buffer=self.serial.read(500)
			if len(rx_buffer)==0:
				return None
			else:
				try:
					message=pickle.loads(rx_buffer)
				except:
					self.error_counter+=1
					continue	

				self.message_counter+=1
				return message
				
			

