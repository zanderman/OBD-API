import socket
from datetime import datetime
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.10',35000))

def setup_device():
    
    print 'Resetting Device: atz'
    s.send('atz\r\n')
    time.sleep(1)
    print s.recv(1024)
    #print s.recv(1024)

    print '\nRemoving Echo: ate0'
    s.send('ate0\r\n')
    print s.recv(1024)

    print '\nRemoving Space Characters from Response'
    s.send('ats0\r\n')
    print s.recv(1024)

    print '\nRemoving Linefeed from Response'
    #s.send('atl0\r\n')
    #print s.recv(1024)

    print '\nRemoving Headers from Response'
    s.send('ath0\r\n')
    print s.recv(1024)

    print '\nVIN: 0902'
    s.send('0902\r\n')
    print s.recv(1024)
    print s.recv(1024)

    print '\nCurrent Protocol: atdp'
    s.send('atdp\r\n')
    print s.recv(1024)

    print '\nReady?: 0100'
    s.send('0105\r\n')
    print s.recv(1024)

def speed_test():
    """Speed test function"""
    print '\nStarting Speed Test'

    numRuns = 5
    starttime = datetime.now()

    # Coolant temperature, expecting 1 byte in return
    s.send('01051\r\n')

    for i in range(0,numRuns):
        #starttime = datetime.now()
        for x in range(0,100): 
            s.send('\r\n')
            s.recv(1024)

    nettime = datetime.now() - starttime
    print "Total time: " + str(nettime)

    avgTimeIteration = nettime/numRuns
    print "Average time per 100 commands: " + str(avgTimeIteration)

    avgTimePerCommand = avgTimeIteration/100
    print "Average time per command: " + str(avgTimePerCommand)

if __name__ == '__main__':

    print 'WiFi OBD-II Speed Tests\n'
    """ WiFi OBD-II Speed Tests """

    # Setup Device
    setup_device()

    # Begin speed test
    speed_test()

    # Put device in Low Power mode
    #send_cmd('atlp')

    s.close()


