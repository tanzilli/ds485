import rs485	
import time

link=rs485.Link("/dev/ttyUSB0")
message2=rs485.Packet(target_node=2,frame_type=rs485.RELAY)
message3=rs485.Packet(target_node=3,frame_type=rs485.RELAY)

while True:
	message2.set_relay_state(1)
	link.send(message2)
	time.sleep(0.4)
        message3.set_relay_state(0)
        link.send(message3)
	time.sleep(1)

	message2.set_relay_state(0)
	link.send(message2)
	time.sleep(0.4)
        message3.set_relay_state(1)
        link.send(message3)
	time.sleep(1)





