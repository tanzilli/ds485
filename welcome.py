from acmepins import GPIO 
from time import sleep
import lcd


backlight=GPIO('J4.19','OUTPUT')
backlight.on()

LCD=lcd.lcd()
LCD.putstring("    DS485")
#LCD.setcurpos(0,1)
#LCD.putstring("by Cipriani Tech")

