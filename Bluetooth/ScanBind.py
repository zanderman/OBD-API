
# Import libraries
import serial
import bluetooth
import os

# Baudrate
BAUD = 115200

###
# Description:  Scan for available BT devices.
# Return:       MAC Address of OBD device.
###
def scan():

  # Discover all available BT devices.
  devices = bluetooth.discover_devices()

	###
	# Find all BT devices that are listed as OBD adapters.
	### 
	for addr in devices:
		name = bluetooth.lookup_name(addr)
		if ( "OBD" in name ):
			print "found '" + name + "' @ " + addr
			return addr


###
# Description:  Runs system commands to bind the OBD device with rfcomm.
# Return:       nothing
###
def bind( addr ):

	###
	# Run through the system process of 
	# trusting the device.
	###
	os.system( "sudo rfcomm release all" )

	cmd = "sudo rfcomm bind 0 " + addr + " 1"
	print cmd
	os.system( cmd )


###
# Main code.
###
if __name__ == '__main__':

	# Scan for devices
	addr = scan()

	# Bind the device to rfcomm
	bind( addr )

	# Create serial connection
	port = serial.Serial('/dev/rfcomm0', BAUD)

	# Write a generic command.
	port.write('01 05\r\n')

  # Read from the connection.
	print port.readline()
	
	# End.
	print "done!"





