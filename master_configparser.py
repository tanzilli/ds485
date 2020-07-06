from ConfigParser import SafeConfigParser
import os

CONFIG_FILE="ds485.ini"
parser = SafeConfigParser()

if os.path.isfile(CONFIG_FILE)==False: 
	parser.add_section('RS485')
	parser.set("RS485","Address","2")
	fd = open(CONFIG_FILE,'w')
	parser.write(fd)
	fd.close()

parser.read(CONFIG_FILE)

parser.set("RS485","Address","3")
fd = open(CONFIG_FILE,'w')
parser.write(fd)
fd.close()
