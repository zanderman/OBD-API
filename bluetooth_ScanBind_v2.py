
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


def get_result():
    buffer = ""
    repeat_count = 0

    while 1:
        c = port.read(1)
        if len(c) == 0:
            if(repeat_count == 5):
                break
            print "Got nothing\n"
            repeat_count = repeat_count + 1
            continue
                    
        if c == '\r':
            continue
                    
        if c == ">":
            break;
                     
        if buffer != "" or c != ">": #if something is in buffer, add everything
            buffer = buffer + c

    return buffer

def send_cmd(cmd):
    if port:
        port.flushOutput()
        port.flushInput()
        for c in cmd:
            port.write(c)
        port.write('\r\n')


###
# Main code.
###
if __name__ == '__main__':

	# Print message
	print 'Scanning for OBDII Devices...'

	# Scan for devices
	addr = scan()

	# Bind the device to rfcomm
	bind( addr )

	# Create serial connection
	port = serial.Serial('/dev/rfcomm0', BAUD)

	# Reset the device
	send_cmd('atz')

  	# Read from the connection.
	print get_result()
	
	# End.
	print "done!"




