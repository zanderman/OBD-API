
###
# Imported Libraries.
###
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def generateLinePlot( x, y, title, xlabel, ylabel, name, ext ):
	"""Create and save an XY Line plot.

	Generates an connected XY plot using the given data.
	"""

	try:
		# Set plot labels
		plt.figure( name )
		plt.ylabel( ylabel )
		plt.xlabel( xlabel )

		# Plot the data.
		plt.plot( x, y )

		# Save the figure.
		plt.savefig( name + "." + ext )

		# Return the name of the plot.
		return name + "." + ext

	except:
		# Plot failure.
		return None

def generateBarPlot( title, xlabel, ylabel, name, ext ):

	"""Create and save an XY Bar plot.

	Generates an XY Bar plot using the given data.
	"""

	try:
		return "blank"

	except:
		# Plot failure.
		return None