from acmepins import GPIO 
from time import sleep

backlight=GPIO('J4.19','OUTPUT')
rele=GPIO("J4.29","OUTPUT")
power_usb=GPIO("J4.31","OUTPUT")
sw_esc=GPIO("J4.39","INPUT")
sw_right=GPIO("J4.35","INPUT")
sw_left=GPIO("J4.37","INPUT")
sw_ok=GPIO("J4.33","INPUT")

power_usb.on()
while True:
	sleep(1)
	backlight.on()
	rele.on()
	sleep(1)
	backlight.off()
	rele.off()
	print "ESC", sw_esc.get_value()
	print "LEFT", sw_left.get_value()
	print "RIGHT", sw_right.get_value()
	print "OK", sw_ok.get_value()


