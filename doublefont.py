import lcd
import time


display=lcd.lcd()
display.backlight_off()
display.setdoublefont()



while True:
	current_time = time.localtime()
	a=time.strftime('%H:%M:%S', current_time)
	display.setcurpos(0,0)
	display.putstring(a)
	time.sleep(0.2)

