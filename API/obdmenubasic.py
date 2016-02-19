import Decoder
# MAIN SECTION OF CODE
Decoder.setup()
cont = 1
Decoder.MenuFxCheck()
Decoder.MainMenu()
number = ""
while(cont == 1):
	number = raw_input("\nSelect a mode (00 - 0A), \n\tSend a code with <SEND XXXX>,\n\tRPM for engine RPM,\n\tSPEED for the vehicle speed, \n\tVIN to display Vehicle Identification Number,\n\tCMV for Control Module Voltage,\n\tTSES for Time Since Engine Start,\n\tDTWM for Distance Traveled with MIL,\n\tNWSCC for Number  of Warmups Since Codes Cleared,\n\tDTSCC for Distance Traveled Since Codes Cleared,\n\tTRWM for Time run with MIL,\n\tTSTCC for Time Since Trouble Codes Cleared,\n\tMENU to display options or \n\tEXIT to exit program\n")
	if (number == "01"):
		print(Decoder.Menu01())
	
	elif (number == "02"):
		print(Decoder.Menu02())
	
	elif (number == "03"):
		print(Decoder.Menu03())
	
	elif (number == "04"):
		print(Decoder.Menu04())
	
	elif (number == "05"):
		print(Decoder.Menu05())
	
	elif (number == "06"):
		print(Decoder.Menu06())
		
	elif (number == "07"):
		print(Decoder.Menu07())
	
	elif (number == "08"):
		print(Decoder.Menu08())
		
	elif (number == "09"):
		print(Decoder.Menu09())
		
	elif (number == "0A"):
		print(Decoder.Menu0A())
		
	elif (number == "MENU"):
		print(Decoder.MainMenu())
	elif (number == "EXIT"):
		cont = 0
	elif (number.startswith('SEND')):
		temp = number.split()
		print(Decoder.SendOBD(temp[1]))
	elif (number == "VIN"):
		print(Decoder.getVIN())
	elif (number == "RPM"):
		print(Decoder.getRPM())
	elif (number == "CMV"):
		print(Decoder.getControlModuleVoltage())
	elif (number == "TSES"):
		print(Decoder.getTimeSinceEngineStart())
	elif (number == "DTWM"):
		print(Decoder.getDistTraveledWithMIL())
	elif (number == "NWSCC"):
		print(Decoder.getNumberofWarmupsSinceCodesCleared())
	elif (number == "SPEED"):
		print(Decoder.getSpeed())
	elif (number == "DTSCC"):
		print(Decoder.getDistTraveledSinceCodesCleared())
	elif (number == "TRWM"):
		print(Decoder.getTimeRunWithMIL())
	elif (number == "TSTCC"):
		print(Decoder.getTimeSinceTroubleCodesCleared())

	else:
		print("Please use one of the specified codes.")