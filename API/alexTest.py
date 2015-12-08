from obd import OBD

DISPLAY_PROTOCOL = 'atdp'

adapter = OBD()

# Map: DisplayProtocol to 'atdp' internally

adapter.send_cmd(DISPLAY_PROTOCOL)
print adapter.get_result()
