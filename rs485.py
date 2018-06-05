import serial
import pickle
import time
from timeit import default_timer as timer

TEMP=2
RELAY_ON=3
RELAY_OFF=4

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
			timeout=0.5,
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
		self.serial.write(payload+"55555")
		print len(payload)
		self.serial.flush()

	def receive(self,timeout=0.5):
		start = timer()
		self.serial.reset_input_buffer()
		rx_buffer=""
		while True:
			if (timer()-start)>timeout:
				return None
			inwaiting=self.serial.inWaiting()		
			if inwaiting>0:
				rx_buffer+=self.serial.read(inwaiting)
				if rx_buffer.find("55555")!=-1:
					try:
						message=pickle.loads(rx_buffer)
						return message
					except:
						self.serial.reset_input_buffer()
						rx_buffer=""
						continue	
				else:
					continue			
			

