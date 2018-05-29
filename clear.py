from acmepins import GPIO 
from time import sleep
import lcd


backlight=GPIO('J4.19','OUTPUT')
backlight.on()

LCD=lcd.lcd()
