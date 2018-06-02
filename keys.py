from acmepins import GPIO 
import time

class KEYS():
	KEY_NONE=0
	KEY_ESC=1
	KEY_LEFT=2
	KEY_RIGHT=3
	KEY_OK=4

	esc=None
	left=None
	right=None
	ok=None

	def __init__(self):
		self.esc=GPIO("J4.39","INPUT")
		self.left=GPIO("J4.37","INPUT")
		self.right=GPIO("J4.35","INPUT")
		self.ok=GPIO("J4.33","INPUT")

	def get(self):
		if self.esc.get_value()==0:
			while self.esc.get_value()==0:
				time.sleep(0.2)
			return self.KEY_ESC
			
		if self.left.get_value()==0:
			while self.left.get_value()==0:
				time.sleep(0.2)
			return self.KEY_LEFT
		
		if self.right.get_value()==0:
			while self.right.get_value()==0:
				time.sleep(0.2)
			return self.KEY_RIGHT
		
		if self.ok.get_value()==0:
			while self.ok.get_value()==0:
				time.sleep(0.2)
			return self.KEY_OK
		
		return self.KEY_NONE	
		
	def hit(self):
		if self.esc.get_value()==0 or self.left.get_value()==0 or self.right.get_value()==0 or self.ok.get_value()==0:
			return True
		else:
			return False				