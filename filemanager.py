
###
# Imported Libraries
###
import csv
import sys


class FileManager:

	"""File interface object"""

	def __init__(self):
		pass

	###
	# Initialize a CSV file as a CSV reader object.
	#
	# Return: 	Every row within the CSV file.
	###
	def readCSV( self, filename ):
		try:
			with open( filename, 'rb' ) as f:

				# Array to store contents of file.
				results = []

				###
				# Obtain all rows within the file.
				###
				for row in csv.reader(f, delimiter=','):
					results.append(row)

				# Close the file object.
				f.close()

				return ( results )
		except:
			return ( None )


	###
	# Write a row of content to the desired CSV file.
	#
	# Return: 	Success/Failure of operation.
	###
	def writeCSV( self, filename, row ):
		try:
			with open( filename, 'awb' ) as f:

				# Write to the CSV file.
				csv.writer( f, dialect='excel', delimiter=',' ).writerow( row )

				# Close the file object.
				f.close()
				return ( True )
		except:
			return ( False )



############
# EXAMPLES #
############

### 
# IMPORTANT:
# Create a new empty file called '__init__.py' within the directory that you are currently working in.
# This will allow you to import custom class files, such as this one, into your project.
###

# # Import file manager class.
# from filemanager import FileManager

# # Create file manager object.
# fm = FileManager()

# # Write.
# fm.writeCSV( 'test.csv', ['head1', 'head2', 'head3'] )
# fm.writeCSV( 'test.csv', ['1', 'a', '!'] )
# fm.writeCSV( 'test.csv', ['2', 'b', '@'] )
# fm.writeCSV( 'test.csv', ['3', 'c', '#'] )

# # Read.
# rows = fm.readCSV( 'test.csv' )
# for row in rows:
# 	print row


