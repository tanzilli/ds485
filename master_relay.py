import rs485	
import time

link=rs485.Link("/dev/ttyUSB0")
outgoing_message=rs485.Packet(target_node=2,frame_type=rs485.RELAY)

while True:
	outgoing_message.set_relay_state(1)
	link.send(outgoing_message)
	time.sleep(1)

	outgoing_message.set_relay_state(0)
	link.send(outgoing_message)
	time.sleep(1)




