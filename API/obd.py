import serial
import os
import socket
import bluetooth
from serial import SerialException

BAUD = 115200

class OBD( ):
        
        def __del__(self):
            # Closes port
            print "Closing port"
            self.port.close()  


        def connect(self):
            # Try creating serial port and receiving data, if failed,
            # connect to the device by rfcomm bind etc.
            try:
                print "Attempting to connect"
                self.port = serial.Serial('/dev/rfcomm0', BAUD)
                # Warm start
                self.send_cmd('atws')
                s = self.get_result()
                print "Device Connected"
                print s
                
            except serial.serialutil.SerialException:
                
                addr = self.scan()
                self.bind(addr)
                self.port = serial.Serial('/dev/rfcomm0', BAUD)
                self.send_cmd('atz')            
                self.get_result()
                print "Device Connected"

        def connect_specific(self,addr):

            print "Attempting to connect"
            self.bind(addr)
            self.port = serial.Serial('/dev/rfcomm0', BAUD)
            self.send_cmd('atz')            
            self.get_result()
            print "Device Connected"
            
        def scan(self):
            # Discover all available BT devices.
            print "Scanning for devices"
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
                        return 1
                else:
                        return 0
        

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
                     
                #if something is in buffer, add everything
                if buffer != "" or c != ">": 
                    buffer = buffer + c

            return buffer

        ## Description: Retrieves result from OBD device            
        # @param        command to send
        # @return       received string
        def send_obd(self,cmd):
            self.send_cmd(cmd)
            return self.get_result()
