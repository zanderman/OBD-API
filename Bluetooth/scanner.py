
# Imported libraries
import bluetooth

###
# Description:  Scan for available BT devices.
# Return:       Array of dictionaries.
###
def scan( key ):
	
	# Discover all available BT devices.
  	devices = bluetooth.discover_devices()

  	# Declare an array for storing resulting dictionaries.
  	results = []

	###
	# Find all BT devices that are listed as OBD adapters.
	### 
 	for addr in devices:
		name = bluetooth.lookup_name(addr)
		if ( key in name ):
			print "found '" + name + "' @ " + addr
			results.append( {'addr':addr, 'name': name } )

	# Return the dictionary array.
	return results

