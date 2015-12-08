import serial
import os
import socket
import bluetooth
from serial import SerialException

BAUD = 115200

class OBD( ):

        def __init__(self):
            # Try creating serial port and receiving data, if failed,
            # connect to the device by rfcomm bind etc.
            try:
                self.port = serial.Serial('/dev/rfcomm0', BAUD)
                self.send_cmd('atdp')
                self.get_result()
                
            except serial.serialutil.SerialException:
                self.connect()

        def __del__(self):

            # Close the serial port
            self.port.close()
            
        def connect(self):
            
            print "Connecting to Bluetooth Device"
            
            addr = self.scan()
            self.bind(addr)
            self.port = serial.Serial('/dev/rfcomm0', BAUD)
            self.send_cmd('atz')            
            print self.get_result()
            
        def scan(self):
            # Discover all available BT devices.
            devices = bluetooth.discover_devices()

            ###
            # Find all BT devices that are listed as OBD adapters.
            ### 
            for addr in devices:
                    name = bluetooth.lookup_name(addr)
                    if ( "OBD" in name ):
                            print "found '" + name + "' @ " + addr
                            return addr

        def bind(self,addr):

            ###
            # Run through the system process of 
            # trusting the device.
            ###
            os.system( "sudo rfcomm release all" )

            cmd = "sudo rfcomm bind 0 " + addr + " 1"
            print cmd
            os.system( cmd )

        ###
        # Description:  Sends command to OBD device
        # Return:       none
        ###
        def send_cmd(self, cmd):
            if self.port:
                self.port.flushOutput()
                self.port.flushInput()
                for c in cmd:
                    self.port.write(c)
                self.port.write('\r\n')

        ###
        # Description:  Retrieves result from OBD device
        # Return:       received string
        ###
        def get_result(self):
            buffer = ""
            repeat_count = 0

            while 1:
                c = self.port.read(1)
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

