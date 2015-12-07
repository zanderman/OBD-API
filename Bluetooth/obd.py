
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
		self.baud = baud
		self.port = None

	def setProtocol( self, proto ):
		self.send('apsp '+str(proto))
		if "OK" in self.receive():
			return True
		else:
			return False


	def send( self, cmd ):
		"""Send a command to the OBD adapter.

		Writes the desired command via a serial connection,
		character by character, until the entire command is 
		sent.

		Return: Success/Failure
		"""

		try:
			if self.port:

				# Clear all serial buffers.
				self.port.flushOutput()
				self.port.flushInput()

				# Send the desired command, one character at a time.
				for c in cmd:
					self.port.write( c )

				# Write ending sequence of characters.
				self.port.write('\r\n')

				# Success!
				return ( True )

			else:
				# Failure
				return ( False )

		except:
			# Failure
			return ( False )


	def receive( self ):
		"""Retrieves result from OBD device.

		Return: received string.
		"""

		buffer = ""
		repeat_count = 0

		try:
			while 1:
				c = self.port.read(1)
				if len(c) == 0:
				    if(repeat_count == 5):
				        break
				    repeat_count = repeat_count + 1
				    continue
				            
				if c == '\r':
				    continue
				            
				if c == ">":
				    break;
				             
				if buffer != "" or c != ">": #if something is in buffer, add everything
				    buffer = buffer + c

			return buffer

		# Lost connection.
		except:
			return ""


	def connect( self ):
		"""Establishes a connection with the OBD adapter.

		Creates a serial conenction on '/dev/rfcomm0' at a 
		pre-specified baudrate.

		Return: Success/Failure
		"""
		try:
			self.port = serial.Serial( '/dev/rfcomm0', self.baud )
			
			# Success!
			return ( True )

		except:
			# Failure
			return ( False )


	def bind( self ):
		"""Binds the OBD adapter with 'rfcomm'

		Run through the system process of 
		trusting the device.

		Return: Success/Failure
		"""

		try:
			# Release all previous rfcomm bindings.
			os.system( "sudo rfcomm release all" )

			# Bind the current OBD object with rfcomm.
			os.system( "sudo rfcomm bind 0 " + self.addr + " 1" )

			# Success!
			return ( True )

		except:
			# Failure
			return ( False )

