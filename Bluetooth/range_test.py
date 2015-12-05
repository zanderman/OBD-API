
###
# Imported Classes.
###
from obd import OBD
from filemanager import FileManager
import scanner

###
# Imported Libraries.
###
from datetime import datetime


# Baudrate
BAUD = 115200

# Total number of graph points.
numIterations = 100

# CSV file name.
csvfile = "rangetest.csv"



###
# Main Testing Code.
###
if __name__ == '__main__':

	"""Bluetooth OBD-II Range Test

	This script manages all range testing of an OBD-II adapter.
	"""

	print "[Begin]\tRange Testing"

	# Scan for all adapters.
	adapters = scanner.scan( "OBD" )

	# Grab the first adapter returned.
	adapter = OBD( adapters[0]['addr'], adapters[0]['name'], BAUD )

	# Setup the file manager.
	fm = FileManager()

	# Write header to CSV file.
	fm.writeCSV( csvfile, [ "Iteration", "RX/TX Time" ] )

	# Save the starting time.
	starttime = datetime.now()

	###
	# Run the range test.
	###
	for i in range( 0, numIterations ):
		
		# Write an empty line.
		adapter.send( "" )
		timesent = datetime.now()

		# Try to receive data.
		rec = adapter.receive()
		timereceive = datetime.now()

		# Save results to CSV file.
		fm.writeCSV( csvfile, [ str(i), str(timereceive-timesent) ] )

	# Get the time when testing completes.
	finishtime = datetime.now()

	# Write ending results.
	print "Time to completion: " + str(starttime - finishtime)
	print "CSV File: " + csvfile

	print "[End]\tRange Testing"