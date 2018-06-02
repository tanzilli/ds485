import rs485	
import time

link=rs485.Link("/dev/ttyS2")
message=rs485.Payload(target_node=2,frame_type=rs485.TEMP)

while True:
	link.send(message)
	sensors_list=link.get()




	time.sleep(1)




