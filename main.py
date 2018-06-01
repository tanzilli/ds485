#!/usr/bin/python

import lcd
import time
import keys
from acmepins import GPIO 
import socket
import ds18b20
from datetime import timedelta
from rs485 import RS485	
from rs485 import RS485_payload
import rs485
import threading


class Slave(threading.Thread):
	stop=False
	
	def __init__(self,link):
		threading.Thread.__init__(self)
		self.link=link

	def run(self):
		while self.stop==False:
			incoming_message=self.link.receive()
			print self.link.get_message_counter(),self.link.get_error_counter()
			
			if incoming_message.get_target_node()==rs485_address:
				if incoming_message.get_frame_type()==rs485.RELAY:
					if incoming_message.get_relay_state()==1:
						relay.on()
					else:
						relay.off()
	def stop(self):
		self.stop=True		

class SensorsReader(threading.Thread):
	stop=False

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while self.stop==False:
			sensors = ds18b20.get_available_sensors();
			total_sensors=len(sensors)
			print total_sensors
			print sensors
			time.sleep(10)
	
	def stop(self):
		self.stop=True		

class ScreenSaver(threading.Thread):
	stop=False

	def __init__(self,timeout):
		threading.Thread.__init__(self)
		self.timeout=timeout
		self.counter=0

	def run(self):
		while self.stop==False:
			time.sleep(1)
			if self.counter>=self.timeout:
				display.backlight_off()
			else:	
				display.backlight_on()
				self.counter+=1

	def reset(self):
		self.counter=0
		display.backlight_on()
		
	def stop(self):
		self.stop=True		
	
def myip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
	local_ip_address = s.getsockname()[0]
	return local_ip_address

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

link=RS485("/dev/ttyUSB0")
SlaveThread=Slave(link)
SlaveThread.start()

ScreenSaverThread=ScreenSaver(60)
ScreenSaverThread.start()

SensorsThread=SensorsReader()
SensorsThread.start()

try:
	while True:
		print total_sensors
		print sensors
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
			display.putstring("DS-485 -- V0.06")		
			current_state=next_state

		if next_state==STATE_TEMPERATURES:
			display.clear()	
			if (current_sensor==-1):
				display.putstring("Sensors: %d" % total_sensors)
			else:
				display.putstring(sensors[current_sensor])
				
			current_state=next_state

			#	for sensor in sensors:
			#		print("Sensor %s has temperature %.2f" % (sensor, ds18b20.get_temperature(sensor)))

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

except:
	print "Exit"

finally:	
	SlaveThread.stop()
	ScreenSaverThread.stop()
	SensorsThread.stop()
	
	SlaveThread.join()
	ScreenSaverThread.join()
	SensorsThread.join()
	
	display.clear()	
	display.setdoublefont()
	display.putstring("Bye, Bye... :-)")
	time.sleep(2)
	display.backlight_off()
	display.clear()	
	
