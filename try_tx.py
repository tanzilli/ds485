import rs486	
import time

link=rs486.Link("/dev/ttyUSB0")

tx_counter=0
while True:
	tx_counter+=1
	print "%d] Tx" % tx_counter
	message=rs486.Packet(1,tx_counter)
	link.send(message)
	time.sleep(0.05)




