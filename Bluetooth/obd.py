
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
	def __init__( self, *args, **kwargs ):

		# Save the adapter type.
		self.type = kwargs.get("type")

		if "wifi" in type:
			self.name = kwargs.get("name")
			self.ip = kwargs.get("ip")
			self.port = kwargs.get("port")
		if "bluetooth" in type:
			self.addr = kwargs.get("addr")
			self.name = kwargs.get("name")
			self.baud = kwargs.get("baud")
			self.port = None

	# def __init__(self, addr, name, baud):
	# 	self.addr = addr
	# 	self.name = name
	# 	self.baud = baud
	# 	self.port = None

	def setProtocol( self, proto ):

		# Send command to change protocol.
		self.send('apsp '+str(proto))

		# Get received data.
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

			# Bluetooth device.
			if "bluetooth" in self.type:

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

			# WiFi device.
			if "wifi" in self.type:
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

			# Bluetooth device.
			if "bluetooth" in self.type:
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

			# WiFi device.
			if "wifi" in self.type:
				return ( "" )

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

			if "bluetooth" in self.type:
				self.port = serial.Serial( '/dev/rfcomm0', self.baud )
			
				# Success!
				return ( True )

			if "wifi" in self.type:
				return ( False )

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

			if "bluetooth" in self.type:
				# Release all previous rfcomm bindings.
				os.system( "sudo rfcomm release all" )

				# Bind the current OBD object with rfcomm.
				os.system( "sudo rfcomm bind 0 " + self.addr + " 1" )

				# Success!
				return ( True )

			if "wifi" in self.type:
				return ( False )

		except:
			# Failure
			return ( False )

