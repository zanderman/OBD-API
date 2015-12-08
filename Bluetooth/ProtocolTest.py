
from obd import OBD
import scanner

import sys

def test():

        for i in range ( 1, 9):
        
                if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ str(i)+" supports this device.\n"
                else:
                        print "\tProtocol "+ str(i)+" doesn't support this device.\n"
                        
        i = "A"
        if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ i +" supports this device.\n"
                else:
                        print "\tProtocol "+ i +" doesn't support this device.\n"
        i = "B"
        if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ i +" supports this device.\n"
                else:
                        print "\tProtocol "+ i +" doesn't support this device.\n"
        i = "C"
        if (adapter.setProtocol(i)) == True:
                        print "\tProtocol "+ i +" supports this device.\n"
                else:
                        print "\tProtocol "+ i +" doesn't support this device.\n"
                        
                        
                        
                        
def __name__ == '__main__':

        adapter = scanner.scan "OBD"
        if len ( adapter ) == 0
                print "[!]\tNo adapters were found that have 'OBD' in their name.\nExiting..."
                
        else:
		            
		adapter = OBD( adapters[0]['addr'], adapters[0]['name'], BAUD )
		adapter.bind()
		adapter.connect()
		test()
