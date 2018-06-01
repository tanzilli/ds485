from rs485 import RS485	
from rs485 import RS485_payload
import rs485	

link=RS485("/dev/ttyUSB0")
polling=RS485_payload(source_node=1,target_node=2,frame_type=rs485.POLLING)

link.send(polling)




