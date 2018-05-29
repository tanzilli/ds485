import lcd
import time

display=lcd.lcd()
display.backlight_on()

#a=100
#for i in range(100):
#	display.setcurpos(0,0)
#	display.putstring("Ospiti: %03d" % (i))
#	display.setcurpos(0,1)
#	display.putstring("Locali: %03d" % (a))
#	time.sleep(0.1)
#	a=a-1

while True:
	current_time = time.localtime()
	a=time.strftime('%H:%M:%S', current_time)
	display.setcurpos(0,0)
	display.putstring(a)
	time.sleep(0.2)
