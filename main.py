import lcd
import time
import keys
from acmepins import GPIO 
import socket
import ds18b20

def myip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
	local_ip_address = s.getsockname()[0]
	return local_ip_address

display=lcd.lcd()
display.backlight_on()
key=keys.KEYS()
rele=GPIO("J4.29","OUTPUT")

STATE_INIT=0
STATE_WELCOME=1
STATE_TEMP=2
STATE_TEST_RELAY=3
STATE_BACKLIGHT=4
STATE_MYIP=5
LAST_STATE=5

current_state=0
next_state=1

while True:
	if current_state==next_state:
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
		continue
		
	if next_state==STATE_WELCOME:
		display.clear()	
		display.putstring("DS485")		
		display.setcurpos(0,1)
		display.putstring("Ver 0.02")
		current_state=next_state

	if next_state==STATE_TEMP:
		display.clear()	
		display.putstring("TEMP")		
		current_state=next_state

	if next_state==STATE_MYIP:
		display.clear()	
		display.putstring("IP address")
		display.setcurpos(0,1)
		display.putstring(myip())
		current_state=next_state

	if next_state==STATE_TEST_RELAY:
		display.clear()	
		display.putstring("TEST RELE")
		display.setcurpos(0,1)
		display.putstring("ESC=OFF    OK=ON")
		current_state=next_state

	if next_state==STATE_BACKLIGHT:
		display.clear()	
		display.putstring("BACKLIGHT")
		display.setcurpos(0,1)
		display.putstring("ESC=OFF    OK=ON")
		current_state=next_state

	continue