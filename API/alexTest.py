from obd import OBD
from at_commands import *

HIREKEN_MAC_ADDR = '00:1D:A5:00:03:43'

adapter = OBD()
#adapter.scan()
#adapter.connect_specific(HIREKEN_MAC_ADDR)
adapter.connect()

print adapter.send_obd(DESC_PROTOCOL)
print adapter.send_obd(ECHO_OFF)
print adapter.send_obd(DISP_DEV_ID)
print adapter.send_obd(REPEAT_CMD)
print adapter.send_obd('010C')
print adapter.send_obd(WARM_START)
print adapter.send_obd('010C')

#adapter = OBD_User()
#adapter.connect()

#print adapter.send_obd(WARM_ATART)