from rs485 import RS485	
from rs485 import RS485_payload
import rs485

link=RS485("/dev/ttyUSB1")

while True:
	incoming_message=link.receive()
	
	print "Messaggio in arrivo"
	print incoming_message
	print incoming_message.get_target_node()
	print incoming_message.get_source_node()
