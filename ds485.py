class DS485_data():
	
	def __init__(self,node_addr):
		self.temperatures={}
		self.node_addr=node_addr

	def put(self,sensor_id,temp):
		self.temperatures[sensor_id]=temp

	def get(self):
		return self.temperatures

	def get_node_addr(self):
		return self.node_addr

	def __str__(self):
		return str(self.temperatures)	
