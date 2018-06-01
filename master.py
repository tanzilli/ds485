from rs485 import RS485	
from rs485 import RS485_payload
import rs485	

link=RS485("/dev/ttyUSB0")
outgoing_message=RS485_payload(source_node=1,target_node=2,frame_type=rs485.POLLING)

outgoing_message.put("1234",12.23)
outgoing_message.put("1111",13.35)
outgoing_message.put("2222",17.13)
outgoing_message.put("0000",20.5)

link.send(outgoing_message)




