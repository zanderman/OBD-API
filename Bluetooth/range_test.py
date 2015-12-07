
###
# Imported Classes.
###
from obd import OBD
from filemanager import FileManager
import scanner
import plotter

###
# Imported Libraries.
###
from datetime import datetime
from time import sleep
import sys


# Baudrate
BAUD = 115200

# Total number of graph points.
numIterations = 1000

# CSV file name.
csvfile = "rangetest.csv"



def test(  ):
	"""Perform the range test.

	Sends/Receives 'N' times and saves the time delay into a CSV file.
	"""

	# Initialize variable for percentage.
	percetage = 0

	###
	# Run through all iterations.
	###
	for i in range( 0, numIterations ):

		# Print out the current percentage.
		if ( i % ( numIterations/100 ) ) == 0:
			print "\r\t" + str(percetage) + "% complete",
			percetage = percetage + 1
		
		if i > 5:
			# Wait for the user to move.
			sleep(0.1)
		
		# Write an empty line.
		adapter.send( "" )
		timesent = datetime.now()

		# Try to receive data.
		rec = adapter.receive()
		timereceive = datetime.now()

		# Save results to CSV file.
		if not len(rec) == 0:
			fm.writeCSV( csvfile, [ str(i), str( (timereceive-timesent).total_seconds() ) ] )
		else:
			fm.writeCSV( csvfile, [ str(i), str( 0 ) ] )


def getColumns( rows ):
	"""Obtains all columns within the CSV file.

	Iterates over all rows within the CSV file and saves
	the different columns into a dictionary using their
	associated header names.
	"""

	# Dictionary of columns.
	cols = {}

	# Array of column header names.
	headers = []

	# Iterate over all rows within the file.
	for i in range( 0, len(rows) ):

		# Save all column names.
		if i == 0:
			for j in range( 0, len(rows[i]) ):
				headers.append( rows[i][j] )
				cols[ headers[ j ] ] = []
		# Populate the columns.
		else:
			for j in range( 0, len(rows[i]) ):
				cols[headers[j]].append( rows[i][j] )

	# Return dictionary of columns
	return cols



###
# Main Testing Code.
###
if __name__ == '__main__':

	"""Bluetooth OBD-II Range Test

	This script manages all range testing of an OBD-II adapter.
	"""

	# Scan for all adapters.
	adapters = scanner.scan( "OBD" )

	# No adapters were found.
	if len( adapters ) == 0:
		print "[!]\tNo adapters were found that have 'OBD' in their name.\nExiting..."

	# Adapters were found.
	else:
		# Grab the first adapter returned.
		adapter = OBD( adapters[0]['addr'], adapters[0]['name'], BAUD )
		adapter.bind()
		adapter.connect()

		# Setup the file manager.
		fm = FileManager()

		# Write header to CSV file.
		fm.writeCSV( csvfile, [ "Iteration", "RX/TX Time" ] )

		print "[Begin]\tRange Testing"

		# Save the starting time.
		starttime = datetime.now()

		###
		# Run the range test.
		###
		test( )

		# Get the time when testing completes.
		finishtime = datetime.now()

		# Create a plot of the values.
		columns = getColumns( fm.readCSV( csvfile ) )

		# Create plot.
		figurename = plotter.generatePlot( columns["Iteration"][1:len(columns["Iteration"])], columns["RX/TX Time"][1:len(columns["RX/TX Time"])], "Range Test", "Iteration", "(RX - TX) Time [sec]", ("rangetest_" + finishtime.strftime( "%H_%M_%S" )), "png" )

		# Write ending results.
		print "\tTime to completion: " + str( finishtime - starttime )
		print "\tCSV File: " + csvfile
		print "\tPlot Image: " + figurename

		print "[End]\tRange Testing"