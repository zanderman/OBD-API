
###
# Imported Libraries
###
import csv
import sys


###
# Initialize a CSV file as a CSV writer object.
###
def getCSVWriter( filename ):
	try:
		return ( csv.writer(open( filename, 'wb' ), dialect='excel', delimiter=',') )
	except:
		return ( None )

###
# Write a row of content to the desired CSV file.
###
def writeCSV( csvwriter, row ):
	try:
		csvwriter.writerow( row )
		return ( True )
	except:
		return ( False )




if __name__ == '__main__':

	# Get CSV object.
	csv = getCSVWriter( 'test.csv' )

	###
	# Write some content to the file.
	###
	writeCSV( csv, ['head1', 'head2', 'head3'] )
	writeCSV( csv, ['1', 'a', '!'] )
	writeCSV( csv, ['2', 'b', '@'] )
	writeCSV( csv, ['3', 'c', '#'] )

	# End test.
	print "done!"


