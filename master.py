from rs485 import RS485	
from rs485 import RS485_payload
import rs485	
import time

link=RS485("/dev/ttyS2")
outgoing_message=RS485_payload(source_node=1,target_node=2,frame_type=rs485.RELAY)


while True:
	outgoing_message.set_relay_state(1)
	link.send(outgoing_message)
	time.sleep(1)

	outgoing_message.set_relay_state(0)
	link.send(outgoing_message)
	time.sleep(1)




