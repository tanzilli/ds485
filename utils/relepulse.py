from acmepins import GPIO 
import time


rele=GPIO("J4.29","OUTPUT")


while True:
	rele.on()
	time.sleep(1)
	rele.off()
	time.sleep(1)