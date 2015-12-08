
from obd import OBD

import scanner
import time
import sys

def test():

        for i in range ( 1, 9):
        
                if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ str(i)+" supports this device.\n"
                else:
                        print "\tProtocol "+ str(i)+" doesn't support this device.\n"
                time.sleep(5)
        i = "A"
        if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ i +" supports this device.\n"
        else:
                        print "\tProtocol "+ i +" doesn't support this device.\n"
        time.sleep(5)
        i = "B"
        if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ i +" supports this device.\n"
        else:
                        print "\tProtocol "+ i +" doesn't support this device.\n"
        time.sleep(5)
        i = "C"
        if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ i +" supports this device.\n"
        else:
                        print "\tProtocol "+ i +" doesn't support this device.\n"
                        
                        
                        
def bluetooth():
	
	adapters = scanner.scan( "OBD" )

	if len( adapters ) == 0:
		print "[!]\tNo adapters were found that have 'OBD' in their name.\nExiting..."

	# Adapters were found.
	else:
		# Grab the first adapter returned.
		# adapter = OBD( adapters[0]['addr'], adapters[0]['name'], BAUD )
		adapter = OBD( type="bluetooth", addr=adapters[0]['addr'], name=adapters[0]['name'], baud=BAUD )
		adapter.bind()
		adapter.connect()
                        
if __name__ == '__main__':

	bluetooth()
	test()
