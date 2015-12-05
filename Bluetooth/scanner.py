
# Imported libraries
import bluetooth

###
# Description:  Scan for available BT devices.
# Return:       Array of (address, name) tuples.
###
def scan( key ):
	
	# Discover all available BT devices.
  	devices = bluetooth.discover_devices()

  	# Declare an array for storing resulting tuples.
  	results = []

	###
	# Find all BT devices that are listed as OBD adapters.
	### 
 	for addr in devices:
		name = bluetooth.lookup_name(addr)
		if ( key in name ):
			print "found '" + name + "' @ " + addr
			results.append( (addr, name) )

	# Return the tuple array.
	return results

