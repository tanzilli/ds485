class Data():
	temperatures={}
	address=-1
	a=111
	
	def __init__(self,address):
		self.address=address
		self.temperatures["9999"]=23
		
	def __getstate__(self):
		print "GetState dict",self.__dict__
		return self.__dict__

	def __setstate__(self, d):
		print "SetState dict",self.__dict__
		self.__dict__ = d

	def save(self,sensor_id,temp):
		self.temperatures[sensor_id]=temp

	def get_data(self):
		return self.temperatures

	def get_address(self):
		return self.address

	def show(self):
		print self.temperatures

		
