from acmepins import GPIO 
from time import sleep
import lcd
import ds18b20


backlight=GPIO('J4.19','OUTPUT')
rele=GPIO("J4.29","OUTPUT")
#power_usb=GPIO("J4.31","OUTPUT")
sw_esc=GPIO("J4.39","INPUT")
sw_right=GPIO("J4.35","INPUT")
sw_left=GPIO("J4.37","INPUT")
sw_ok=GPIO("J4.33","INPUT")

#power_usb.on()

backlight.on()

LCD=lcd.lcd()
LCD.putstring("    DS485")
LCD.setcurpos(0,1)
LCD.putstring("by Cipriani Tech")

