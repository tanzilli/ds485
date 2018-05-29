import lcd
import time
import keys
from acmepins import GPIO 

display=lcd.lcd()
display.backlight_on()
key=keys.KEYS()
rele=GPIO("J4.29","OUTPUT")

STATE_INIT=0
STATE_TEST_RELAY=3
STATE_BACKLIGHT=4

# 0 = Init
# 1 = Welcome message

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
			if current_state<4:
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
		
	if next_state==1:
		display.clear()	
		display.putstring("DS485")		
		display.setcurpos(0,1)
		display.putstring("Ver 0.1")
		current_state=1

	if next_state==2:
		display.clear()	
		display.putstring("TEMP")		
		current_state=2

	if next_state==STATE_TEST_RELAY:
		display.clear()	
		display.putstring("TEST RELE")
		display.setcurpos(0,1)
		display.putstring("ESC=OFF    OK=ON")
		current_state=STATE_TEST_RELAY

	if next_state==STATE_BACKLIGHT:
		display.clear()	
		display.putstring("BACKLIGHT")
		display.setcurpos(0,1)
		display.putstring("ESC=OFF    OK=ON")
		current_state=STATE_BACKLIGHT


	continue