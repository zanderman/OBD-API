## @package OBD API
# This module features the OBD API implementation
# This module allows a user to scan, bind, and connect
# to wireless bluetooth OBD adapter, as well as 
# to communicate with the daapter by sending and
# receiving commands.

import serial
import os
import socket
import bluetooth
from serial import SerialException

BAUD = 115200

class OBD( ):
        
        ## The destructor of this class closes
        # any ports that may have been opened
        # @param self the object pointer
        def __del__(self):
            
            print "Closing port"
            self.port.close()  

        ## Try creating a serial port and receive data, if failed
        # connect to the device by scanning for all bluetooth devices,
        # parsing out the string "OBD" and binding with rfcomm.
        # @param self the object pointer
        def connect(self):
            
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

        ## Connect to a specific device with a known
        # mac address.
        # @param self the object pointer
        # @param addr the mac address of device
        def connect_specific(self,addr):
            
            print "Attempting to connect"
            self.bind(addr)
            self.port = serial.Serial('/dev/rfcomm0', BAUD)
            self.send_cmd('atz')            
            self.get_result()
            print "Device Connected"
        
        ## Discover all bluetooth devices
        # @param self the object pointer
        # @return the address of found OBD device   
        def scan(self):
            
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

        ## Run through the system process of trusting the device.
        # @param self the object pointer
        # @param addr the mac address of device
        def bind(self,addr):
            
            
            os.system( "sudo rfcomm release all" )

            cmd = "sudo rfcomm bind 0 " + addr + " 1"
            os.system( cmd )

        ## Send a command to the OBD device
        # @param self the object pointer
        # @param cmd any acceptable command from datasheet
        # such as PID command or at command
        # @return boolean for success or failure
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
        

        ## Retrieve data from the OBD device, this is
        # usually preceeded by a "send_cmd"
        # @param self the object pointer
        # @return received string
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

        ## Description: Sends command and retrieves 
        #result from OBD device            
        # @param cmd  command to send
        # @param self the object pointer
        # @return     received string
        def send_obd(self,cmd):
            self.send_cmd(cmd)
            return self.get_result()
