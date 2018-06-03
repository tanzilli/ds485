#!/usr/bin/python

import lcd
import time
import keys
from acmepins import GPIO 
import socket
from datetime import timedelta
import rs485
import threading
import os

class SensorsReader(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.stop_flag=False
		self.reading=False
		self.writing=False
		self.sensors = {}
		
	def run(self):
		while self.stop_flag==False:
			sensors_live = {}
			#print "---"
			for sensor in os.listdir("/sys/bus/w1/devices"):
				if sensor.startswith("28-"):
					sensor_id=sensor[3:]
					sensors_live[sensor_id]=self.get_temperature(sensor_id)
					#print sensor_id,sensors_live[sensor_id]
					
			while self.reading==True:
				print "Wait"
				time.sleep(0.1)
			self.writing=True
			self.sensors=sensors_live
			self.writing=False
	
	def sensors_list(self):
		self.reading=True
		while self.writing==True:
			time.sleep(0.1)
		ret=self.sensors
		self.reading=False
		return ret

	def sensors_available(self):
		return len(self.sensors)

	def get_temperature(self,sensor_id):
		try:
			with open("/sys/bus/w1/devices/28-" + sensor_id + "/w1_slave") as f:
				data = f.readlines()
			if data[0].strip()[-3:] != "YES":
				return 999
			else:	
				return float(data[1].split("=")[1])*0.001
		except:
			return 999

	def stop(self):
		self.stop_flag=True	

class LinkManager(threading.Thread):
	def __init__(self,link):
		threading.Thread.__init__(self)
		self.stop_flag=False
		self.link=link

	def run(self):
		while self.stop_flag==False:
			incoming_message=self.link.receive()
			
			print "-"

			if incoming_message==None:
				continue
				
			print "--"
				
			#  print self.link.get_message_counter(),self.link.get_error_counter()
			
			# If any error on packet incomes, just continue
			try:
				if incoming_message.get_target_node()==rs485_address:

					print "---"

					if incoming_message.get_frame_type()==rs485.RELAY:
						if incoming_message.get_relay_state()==1:
							relay.on()
						else:
							relay.off()

					if incoming_message.get_frame_type()==rs485.TEMP:
						outgoing_message=rs485.Packet(target_node=0,frame_type=rs485.TEMP)
						sensors=SensorsReaderThread.sensors_list()
						outgoing_message.put(sensors)
						self.link.send(outgoing_message)
			except:
				continue
									
	def stop(self):
		self.stop_flag=True	

class ScreenSaver(threading.Thread):
	def __init__(self,timeout):
		threading.Thread.__init__(self)
		self.timeout=timeout
		self.counter=0
		self.stop_flag=False

	def run(self):
		while self.stop_flag==False:
			time.sleep(1)
			if self.timeout==-1:
				continue
			if self.counter>=self.timeout:
				display.backlight_off()
			else:	
				display.backlight_on()
				self.counter+=1

	def reset(self):
		self.counter=0
		display.backlight_on()
		
	def stop(self):
		self.stop_flag=True	
	
def myip():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
		local_ip_address = s.getsockname()[0]
		return local_ip_address
	except:
		return "NO IP"	

def uptime():
	with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
		uptime_string = str(timedelta(seconds = uptime_seconds))

	return(uptime_string)

display=lcd.lcd()
display.backlight_on()
key=keys.KEYS()
relay=GPIO("J4.29","OUTPUT")

STATE_INIT=0
STATE_WELCOME=1
STATE_MYADDR=2
STATE_TEMPERATURES=3
STATE_MYIP=4
STATE_UPTIME=5
STATE_ERRORS=6
STATE_TEST_RELAY=7
STATE_BACKLIGHT=8
LAST_STATE=8

current_state=0
next_state=1
rs485_address=2
total_sensors=0
current_sensor=-1
sensors=[]

link=rs485.Link("/dev/ttyS2")
LinkManagerThread=LinkManager(link)
LinkManagerThread.start()

# Screen saver delay in sec
# -1 = Disabled
ScreenSaverThread=ScreenSaver(120)
ScreenSaverThread.start()

SensorsReaderThread=SensorsReader()
SensorsReaderThread.start()

try:
	delay_temperature=0
	while True:
		time.sleep(0.1)
		a=key.get()
		if a==key.KEY_ESC:
			ScreenSaverThread.reset()
			if current_state>1:
				next_state=current_state-1
			else:
				next_state=LAST_STATE	
				
		if a==key.KEY_OK:
			ScreenSaverThread.reset()
			if current_state<LAST_STATE:
				next_state=current_state+1
			else:
				next_state=1	
				
		if a==key.KEY_LEFT:
			ScreenSaverThread.reset()
			if current_state==STATE_TEST_RELAY:
				relay.off()
			if current_state==STATE_BACKLIGHT:
				display.backlight_off()
			if current_state==STATE_MYADDR:
				if rs485_address>1:
					rs485_address-=1
				else:	
					rs485_address=100
			if current_state==STATE_TEMPERATURES:
				if current_sensor>=0:
					current_sensor-=1

		if a==key.KEY_RIGHT:
			ScreenSaverThread.reset()
			if current_state==STATE_TEST_RELAY:
				relay.on()
			if current_state==STATE_BACKLIGHT:
				display.backlight_on()
			if current_state==STATE_MYADDR:
				if rs485_address<100:
					rs485_address+=1
				else:	
					rs485_address=1
			if current_state==STATE_TEMPERATURES:
				if current_sensor<(len(sensors)-1):
					current_sensor-=1
		
		if next_state==STATE_WELCOME and current_state!=STATE_WELCOME:
			display.clear()	
			display.setdoublefont()
			display.putstring("DS-485 -- V0.10")		
			current_state=next_state

		if next_state==STATE_TEMPERATURES:
			sensors=SensorsReaderThread.sensors_list();	

			counter=0
			for sensor_id in sensors:
				display.clear()	
				if sensors[sensor_id]!=999:
					counter+=1
					display.putstring("%2d- %s" % (counter,sensor_id))
					display.setcurpos(0,1)
					display.putstring("    %.2f C" % sensors[sensor_id])
				
					for i in range(10):	
						time.sleep(0.1)
						if key.hit():
							break

				if key.hit():
					break

			current_state=next_state

		if next_state==STATE_MYADDR:
			display.clear()	
			display.setdoublefont()
			display.putstring("Addr: %d" % rs485_address)
			current_state=next_state

		if next_state==STATE_MYIP:
			display.clear()	
			display.putstring("IP address")
			display.setcurpos(0,1)
			display.putstring(myip())
			current_state=next_state

		if next_state==STATE_UPTIME:
			display.clear()	
			display.putstring("Uptime")
			display.setcurpos(0,1)
			a=uptime()
			display.putstring(a[:a.rfind(".")])
			current_state=next_state

		if next_state==STATE_ERRORS:
			display.clear()	
			display.putstring("Msg/Err")
			display.setcurpos(0,1)
			display.putstring("%d/%d" % (link.get_message_counter(),link.get_error_counter()))
			current_state=next_state

		if next_state==STATE_TEST_RELAY and current_state!=STATE_TEST_RELAY:
			display.clear()	
			display.putstring("Relay")
			display.setcurpos(0,1)
			display.putstring("OFF <-     -> ON")
			current_state=next_state

		if next_state==STATE_BACKLIGHT and current_state!=STATE_BACKLIGHT:
			display.clear()	
			display.putstring("Backlight")
			display.setcurpos(0,1)
			display.putstring("OFF <-     -> ON")
			current_state=next_state

		continue

except KeyboardInterrupt:
	print "Exit"

finally:	
	LinkManagerThread.stop()
	ScreenSaverThread.stop()
	SensorsReaderThread.stop()
	
	LinkManagerThread.join()
	ScreenSaverThread.join()
	SensorsReaderThread.join()
	
	display.clear()	
	display.setdoublefont()
	display.putstring("Bye, Bye... :-)")
	time.sleep(1)
	display.backlight_off()
	display.clear()	
	
