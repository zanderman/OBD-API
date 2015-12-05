
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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Baudrate
BAUD = 115200

# Total number of graph points.
numIterations = 100

# CSV file name.
csvfile = "rangetest.csv"



def generatePlot( rows ):

	# Declare column variables.
	iteration = []
	time = []

	# Iterate over all rows to populate the columns.
	for row in rows:
		if not "Iteration" in row or not "RX/TX Time" in row and not row[0]=='0':
			iteration.append( row[0] )
			time.append( row[1] )

	# Generate plot.
	figurename = ("RangeTest_%H:%M:%S").format(datetime.now())
	plt.figure( figurename )
	plt.ylabel("(RX - TX) Time [sec]")
	plt.xlabel("Iteration")
	plt.plot( iteration, time )
	plt.savefig( figurename + ".png" )

	# Return the name of the plot.
	return figurename





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
	adapter.bind()
	adapter.connect()

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
		fm.writeCSV( csvfile, [ str(i), str( (timereceive-timesent).total_seconds() ) ] )

	# Create a plot of the values.
	figurename = generatePlot( fm.readCSV( csvfile ) )

	# Get the time when testing completes.
	finishtime = datetime.now()

	# Write ending results.
	print "\tTime to completion: " + str( finishtime - starttime )
	print "\tCSV File: " + csvfile
	print "\tPlot Image: " + figurename

	print "[End]\tRange Testing"