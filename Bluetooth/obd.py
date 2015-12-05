
###
# Imported Libraries
###
import serial
import os

class OBD( ):
	"""Representation of an OBD adapter object

	Parameter: 	addr 	MAC address of the adapter.
	Parameter: 	name 	Name of the adapter.
	Parameter: 	baud 	Desired baudrate of the adapter.
	"""
	def __init__(self, addr, name, baud):
		self.addr = addr
		self.name = name
		this.baud = baud
		this.port = None

	def setProtocol( proto ):
		pass

	def send( cmd ):
		"""Send a command to the OBD adapter.

		Writes the desired command via a serial connection,
		character by character, until the entire command is 
		sent.

		Return: Success/Failure
		"""

		try:
			if this.port:

				# Clear all serial buffers.
				this.port.flushOutput()
				this.port.flushInput()

				# Send the desired command, one character at a time.
				for c in cmd:
					this.port.write( c )

				# Write ending sequence of characters.
				this.port.write('\r\n')

				# Success!
				return ( True )

			else:
				# Failure
				return ( False )

		except:
			# Failure
			return ( False )


	def receive( ):
		"""Retrieves result from OBD device.

		Return: received string.
		"""

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


	def connect( ):
		"""Establishes a connection with the OBD adapter.

		Creates a serial conenction on '/dev/rfcomm0' at a 
		pre-specified baudrate.

		Return: Success/Failure
		"""
		try:
			this.port = serial.Serial( '/dev/rfcomm0', this.baud )
			
			# Success!
			return ( True )

		except:
			# Failure
			return ( False )


	def bind():
		"""Binds the OBD adapter with 'rfcomm'

		Run through the system process of 
		trusting the device.

		Return: Success/Failure
		"""

		try:
			# Release all previous rfcomm bindings.
			os.system( "sudo rfcomm release all" )

			# Bind the current OBD object with rfcomm.
			os.system( "sudo rfcomm bind 0 " + this.addr + " 1" )

			# Success!
			return ( True )

		except:
			# Failure
			return ( False )

