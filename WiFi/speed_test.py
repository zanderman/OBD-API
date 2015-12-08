import socket
from datetime import datetime
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.10',35000))

def setup_device():
    
    print 'Resetting Device: atz'
    send_cmd('atz')
    print get_result()

    print '\nRemoving Echo: ate0'
    send_cmd('ate0')
    print get_result()

    print '\nRemoving Space Characters from Response'
    send_cmd('ats0')
    print get_result()

    print '\nRemoving Linefeed from Response'
    send_cmd('atl0')
    print get_result()

    print '\nRemoving Headers from Response'
    send_cmd('ath0')
    print get_result()

    print '\nVIN: 0902'
    send_cmd('0902')
    print get_result()

    print '\nSet protocol automatic: atsp0'
    send_cmd('atsp0')
    print get_result()
    
    print '\nCurrent Protocol: atdp'
    send_cmd('atdp')
    print get_result()

    print '\nReady?: 0100'
    send_cmd('0105')
    print get_result()

def set_baudrate():
    print 'Setting Baud Rate: 115200'
    #send_cmd('atbrd23')
    #print get_result()

    #s.write('\r\n')
    #print get_result()
    send_cmd('atpp0csv23')
    send_cmd('atpp0con')
    send_cmd('atz')
    print get_result()

def send_cmd(cmd):
    """ This function sends a command in 
    the form of a string to the remote
    OBD device"""
    if s:
        #s.flushOutput()
        #s.flushInput()
        for c in cmd:
            s.send(c)
        s.send('\r\n')

def get_result():
    """ This function retrieves the results
    from the remote OBD device"""
    buffer = ""
    repeat_count = 0

    while 1:
        c = s.recv(1)
        if len(c) == 0:
            if(repeat_count == 5):
                break
            print "Got nothing\n"
            repeat_count = repeat_count + 1
            continue
                    
        if c == '\r':
            continue
                    
        if c == ">":
            break;
                     
        if buffer != "" or c != ">": #if something is in buffer, add everything
            buffer = buffer + c

    return buffer


def speed_test():
    """Speed test function"""
    print '\nStarting Speed Test'

    numRuns = 5
    starttime = datetime.now()

    # Coolant temperature, expecting 1 command in return
    s.send('01051\r\n')
    get_result()
    #print get_result()

    for i in range(0,numRuns):
        #starttime = datetime.now()
        for x in range(0,100): 
            s.send('01051\r\n')
            get_result()
            #print get_result()

    nettime = datetime.now() - starttime
    print "Total time: " + str(nettime)

    avgTimeIteration = nettime/numRuns
    print "Average time per 100 commands: " + str(avgTimeIteration)

    avgTimePerCommand = avgTimeIteration/100
    print "Average time per command: " + str(avgTimePerCommand)

if __name__ == '__main__':

    print 'WiFi OBD-II Speed Tests\n'
    """ WiFi OBD-II Speed Tests """

    #set_baudrate()
    # Setup Device
    setup_device()

    # Begin speed test
    speed_test()

    #print '\nRemoving Space Characters from Response'
    #s.send('ats0\r\n')
    #print s.recv(1024)

    #speed_test()

    # Put device in Low Power mode
    #send_cmd('atlp')

    s.close()


