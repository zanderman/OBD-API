
###
# Imported Classes.
###
from obd import OBD
import scanner

# Baudrate
BAUD = 115200

###
# Main Testing Code.
###
if __name__ == '__main__':

	print "[Begin]\tRange Testing"

	# Scan for all adapters.
	adapters = scanner.scan( "OBD" )

	# Grab the first adapter returned.
	adapter = OBD( adapters[0]['addr'], adapters[0]['name'], BAUD )

	# Send and recieve data.
	adapter.send( "atz" )
	print adapter.receive()

	print "[End]\tRange Testing"