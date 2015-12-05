
# Imported libraries
import bluetooth

###
# Description:  Scan for available BT devices.
# Return:       MAC Address of OBD device.
###
def scan( key ):
	
	# Discover all available BT devices.
  	devices = bluetooth.discover_devices()

	###
	# Find all BT devices that are listed as OBD adapters.
	### 
 	for addr in devices:
		name = bluetooth.lookup_name(addr)
		if ( key in name ):
			print "found '" + name + "' @ " + addr
			return addr

