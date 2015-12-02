import serial
import os
from datetime import datetime

s = serial.Serial('/dev/rfcomm0',115200)

def get_result():
    buffer = ""
    repeat_count = 0

    while 1:
        c = s.read(1)
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

def send_cmd(cmd):
    if s:
        s.flushOutput()
        s.flushInput()
        for c in cmd:
            s.write(c)
        s.write('\r\n')


print 'Bluetooth OBD-II Interfacing\n'

print 'Resetting Device: atz'
send_cmd('atz')
print get_result()

print '\nRemoving Echo: ate0'
send_cmd('ate0')
print get_result()

print '\nCurrent Protocol: atdp'
send_cmd('atdp')
print get_result()

print '\nReady?: 0100'
send_cmd('0105')
print get_result()

print 'Starting For Loop'


for i in range(0,5):
    starttime = datetime.now()
    for x in range(0,100): 
        send_cmd('0105')
        get_result()

    print(datetime.now() - starttime)

s.close()

