import lcd
import time
import keys
from acmepins import GPIO 
import socket
import ds18b20
from datetime import timedelta

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
rele=GPIO("J4.29","OUTPUT")

STATE_INIT=0
STATE_WELCOME=1
STATE_TEMP=2
STATE_MYIP=3
STATE_UPTIME=4
STATE_CLOCK=5
STATE_TEST_RELAY=6
STATE_BACKLIGHT=7
LAST_STATE=7

current_state=0
next_state=1

while True:
	time.sleep(0.1)
	a=key.get()
	if a==key.KEY_LEFT:
		if current_state>1:
			next_state=current_state-1
			
	if a==key.KEY_RIGHT:
		if current_state<LAST_STATE:
			next_state=current_state+1
			
	if a==key.KEY_ESC:
		if current_state==STATE_TEST_RELAY:
			rele.off()
		if current_state==STATE_BACKLIGHT:
			display.backlight_off()

	if a==key.KEY_OK:
		if current_state==STATE_TEST_RELAY:
			rele.on()
		if current_state==STATE_BACKLIGHT:
			display.backlight_on()
		
	if next_state==STATE_WELCOME and current_state!=STATE_WELCOME:
		display.clear()	
		display.putstring("DS485")		
		display.setcurpos(0,1)
		display.putstring("Ver 0.02")
		current_state=next_state

	if next_state==STATE_TEMP:
		display.clear()	
		display.putstring("Temperature")		

		sensors = ds18b20.get_available_sensors();
		display.setcurpos(0,1)
		display.putstring("Total sensor %d" % len(sensors))

		#time.sleep(1)
		#for sensor in sensors:
		#	print("Sensor %s has temperature %.2f" % (sensor, ds18b20.get_temperature(sensor)))

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

	if next_state==STATE_CLOCK:
		current_time = time.localtime()
		a=time.strftime('%H:%M:%S', current_time)
		display.clear()	
		display.putstring("Clock")
		display.setcurpos(0,1)
		display.putstring(a)
		current_state=next_state

	if next_state==STATE_TEST_RELAY and current_state!=STATE_TEST_RELAY:
		display.clear()	
		display.putstring("Relay")
		display.setcurpos(0,1)
		display.putstring("ESC=OFF    OK=ON")
		current_state=next_state

	if next_state==STATE_BACKLIGHT and current_state!=STATE_BACKLIGHT:
		display.clear()	
		display.putstring("Backlight")
		display.setcurpos(0,1)
		display.putstring("ESC=OFF    OK=ON")
		current_state=next_state

	continue