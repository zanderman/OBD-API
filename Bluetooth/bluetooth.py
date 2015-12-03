#!/usr/bin/python


# Import the bluetooth library
import bluetooth

# Get a list of BT devices that are within range.
devices = bluetooth.discover_devices()

# Iterate over all devices found.
for addr in devices:
	# Print the device name and its address.
	print "found: " + bluetooth.lookup_name(addr) + " @ " + addr

###
# Use these commands to establish a socket
# and connect to a specific (address,port) pair.
###
#btSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#btSocket.connect((btID, port)) # note: port=3
#btSocket.close()
