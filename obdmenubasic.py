
global B01_20
global B21_40
global B41_60
global B61_80
global B81_A0
global BA1_C0
global BC1_E0




def SendOBD(code):
	print("Sending OBDII CODE: " + str(code))
	# send OBDII CODE

def MenuFxCheck():
	# send 0100 to check 01-20
	# assign B01_20 accordingly
	B01_20 = 0xFFFFFFFF
	# send 0120 to check 21-40
	# assign B21_40 accordingly
	B21_40 = 0xFFFFFFFF
	# send 0140 to check 41-60
	# assign B41_60 accordingly
	B41_60 = 0xFFFFFFFF
	# send 0160 to check 61-80
	# assign B61_80 accordingly
	B61_80 = 0xFFFFFFFF
	# send 0180 to check 81-A0
	# assign B81_A0 accordingly
	B81_A0 = 0xFFFFFFFF
	# send 01A0 to check A1-C0
	# assign BA1_C0 accordingly
	BA1_C0 = 0xFFFFFFFF
	# send 01C1 to check C1-E0
	# assign BC1_E0 accordingly
	BC1_E0 = 0xFFFFFFFF
	
def MainMenu():
	print("Mode Number \tMode Description")
	print("\t 01\tCurrent Data")
	print("\t 02\tFreeze Frame Data")
	print("\t 03\tDiagnostic Trouble Codes")
	print("\t 04\tClear Trouble Code")
	print("\t 05\tTest Results / Oxygen Sensors")
	print("\t 06\tTest Results / Non-continuous Testing")
	print("\t 07\tShow Pending Trouble Codes")
	print("\t 08\tSpecial Control Mode")
	print("\t 09\tRequest Vehicle Information")
	print("\t 0A\tRequest Permanent Trouble Codes\n")
	

def Menu01():
	print("PID \t\t Description")
	print("\t 00\tPIDs supported [01 - 20]")
	if (B01_20 & 0x80000000):
		print("\t 01\tMonitor status since DTCs cleared")
	if (B01_20 & 0x40000000):
		print("\t 02\tFreeze DTC")
	if (B01_20 & 0x20000000):
		print("\t 03\tFuel system status")
	if (B01_20 & 0x10000000):
		print("\t 04\tCalculated engine load value")
	if (B01_20 & 0x08000000):
		print("\t 05\tEngine coolant temperature")
	if (B01_20 & 0x04000000):
		print("\t 06\tShort term fuel % trim-Bank 1")
	if (B01_20 & 0x02000000):
		print("\t 07\tLong term fuel % trim-Bank 1")
	if (B01_20 & 0x01000000):
		print("\t 08\tShort term fuel % trim-Bank 2")
	if (B01_20 & 0x00800000):
		print("\t 09\tLong term fuel % trim-Bank 2")
	if (B01_20 & 0x00400000):
		print("\t 0A\tFuel pressure")
	if (B01_20 & 0x00200000):
		print("\t 0B\tIntake manifold absolute pressure")
	if (B01_20 & 0x00100000):
		print("\t 0C\tEngine RPM")
	if (B01_20 & 0x00080000):
		print("\t 0D\tVehicle speed")
	if (B01_20 & 0x00040000):
		print("\t 0E\tTiming advance")
	if (B01_20 & 0x00020000):
		print("\t 0F\tIntake air temperature\n")
	
	if (B01_20 & 0x00010000):
		print("\t 10\tMAF air flow rate")
	if (B01_20 & 0x00008000):
		print("\t 11\tThrottle position")
	if (B01_20 & 0x00004000):
		print("\t 12\tCommanded Secondary air status")
	if (B01_20 & 0x00002000):
		print("\t 13\tOxygen sensors present")
	if (B01_20 & 0x00001000):
		print("\t 14\tBank 1, Sensor 1: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000800):
		print("\t 15\tBank 1, Sensor 2: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000400):
		print("\t 16\tBank 1, Sensor 3: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000200):
		print("\t 17\tBank 1, Sensor 4: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000100):
		print("\t 18\tBank 2, Sensor 1: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000080):
		print("\t 19\tBank 2, Sensor 2: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000040):
		print("\t 1A\tBank 2, Sensor 3: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000020):
		print("\t 1B\tBank 2, Sensor 4: Oxygen sensor Voltage, Short term fuel trim")
	if (B01_20 & 0x00000010):
		print("\t 1C\tOBD standards this vehicle conforms to")
	if (B01_20 & 0x00000008):
		print("\t 1D\tOxygen sensors present")
	if (B01_20 & 0x00000004):
		print("\t 1E\tAuxiliary input status")
	if (B01_20 & 0x00000002):
		print("\t 1F\tRun time since engine start\n")
	
	print("\t 20\tPIDs supported [21 - 40]")
	print("\t 21\tDistance traveled with malfunction indicator lamp (MIL) on")
	print("\t 22\tFuel rail Pressure (relative to manifold vacuum)")
	print("\t 23\tFuel rail Pressure (diesel, or gasoline direct inject)")
	print("\t 24\tO2S1_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 25\tO2S2_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 26\tO2S3_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 27\tO2S4_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 28\tO2S5_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 29\tO2S6_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 2A\tO2S7_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 2B\tO2S8_WR_lambda(1): Equivalence Ratio Voltage")
	print("\t 2C\tCommanded EGR")
	print("\t 2D\tEGR Error")
	print("\t 2E\tCommanded evaporative purge")
	print("\t 2F\tFuel Level Input\n")
	
	print("\t 30\t# of warm-ups since codes cleared")
	print("\t 31\tDistance traveled since codes cleared")
	print("\t 32\tEvap. System Vapor Pressure")
	print("\t 33\tBarometric pressure")
	print("\t 34\t02S1_WR_lambda(1) Equivalence Ratio Current")
	print("\t 35\t02S2_WR_lambda(1) Equivalence Ratio Current")
	print("\t 36\t02S3_WR_lambda(1) Equivalence Ratio Current")
	print("\t 37\t02S4_WR_lambda(1) Equivalence Ratio Current")
	print("\t 38\t02S5_WR_lambda(1) Equivalence Ratio Current")
	print("\t 39\t02S6_WR_lambda(1) Equivalence Ratio Current")
	print("\t 3A\t02S7_WR_lambda(1) Equivalence Ratio Current")
	print("\t 3B\t02S8_WR_lambda(1) Equivalence Ratio Current")
	print("\t 3C\tCatalyst Temperature Bank 1, Sensor 1")
	print("\t 3D\tCatalyst Temperature Bank 2, Sensor 1")
	print("\t 3E\tCatalyst Temperature Bank 1, Sensor 2")
	print("\t 3F\tCatalyst Temperature Bank 2, Sensor 2\n")
	
	print("\t 40\tPIDs Supported [41 - 60]")
	print("\t 41\tMonitor status this drive cycle")
	print("\t 42\tControl module voltage")
	print("\t 43\tAbsolute load value")
	print("\t 44\tFuel / Air commanded equivalence ratio")
	print("\t 45\tRelative throttle position")
	print("\t 46\tAmbient air temperature")
	print("\t 47\tAbsolute throttle position B")
	print("\t 48\tAbsolute throttle position C")
	print("\t 49\tAccelerator pedal position D")
	print("\t 4A\tAccelerator pedal position E")
	print("\t 4B\tAccelerator pedal position F")
	print("\t 4C\tCommanded throttle actuator")
	print("\t 4D\tTime run with MIL on")
	print("\t 4E\tTime since trouble codes cleared")
	print("\t 4F\tMaximum value for equivalence ratio, oxygen sensor voltage, oxygen sensor current, and intake manifold absolute pressure\n")
	
	print("\t 50\tMaximum value for air flow rate from mass air flow sensor")
	print("\t 51\tFuel Type")
	print("\t 52\tEthanol fuel %")
	print("\t 53\tAbsolute Evap System Vapor Pressure")
	print("\t 54\tEvap system vapor pressure")
	print("\t 55\tShort term secondary oxygen sensor trim bank 1 and bank 3")
	print("\t 56\tLong term secondary oxygen sensor trim bank 1 and bank 3")
	print("\t 57\tShort term secondary oxygen sensor trim bank 2 and bank 4")
	print("\t 58\tLong term secondary oxygen sensor trim bank 2 and bank 4")
	print("\t 59\tFuel rail pressure (absolute)")
	print("\t 5A\tRelative accelerator pedal position")
	print("\t 5B\tHybrid battery pack remaining life")
	print("\t 5C\tEngine oil temperature")
	print("\t 5D\tFuel injection timing")
	print("\t 5E\tEngine fuel rate")
	print("\t 5F\tEmission requirements to which vehicle is designed\n")
	
	print("\t 60\tPIDs supported [61-80]")
	print("\t 61\tDriver's demand engine - percent torque")
	print("\t 62\tActual engine - percent torque")
	print("\t 63\tEngine reference torque")
	print("\t 64\tEngine percent torque data")
	print("\t 65\tAuxiliary input / output supported")
	print("\t 66\tMass air flow sensor")
	print("\t 67\tEngine coolant temperature")
	print("\t 68\tIntake air temperature sensor")
	print("\t 69\tCommanded EGR and EGR Error")
	print("\t 6A\tCommanded Diesel intake air flow control and relative intake air flow position")
	print("\t 6B\tExhaust gas recirculation temperature")
	print("\t 6C\tCommanded throttle actuator control and relative throttle position")
	print("\t 6D\tFuel pressure control system")
	print("\t 6E\tInjection pressure control system")
	print("\t 6F\tTurbocharger compressor inlet pressure\n")
	
	print("\t 70\tBoost pressure control")
	print("\t 71\tVariable Geometry turbo (VGT) control")
	print("\t 72\tWastegate control")
	print("\t 73\tExhaust pressure")
	print("\t 74\tTurbocharger RPM")
	print("\t 75\tTurbocharger temperature")
	print("\t 76\tTurbocharger temperature")
	print("\t 77\tCharge air cooler temperature (CACT)")
	print("\t 78\tExhaust Gas temperature (EGT) Bank 1")
	print("\t 79\tExhaust Gas temperature (EGT) Bank 2")
	print("\t 7A\tDiesel particulate filter (DPF)")
	print("\t 7B\tDiesel particulate filter (DPF)")
	print("\t 7C\tDiesel Particulate filter (DPF) temperature")
	print("\t 7D\tNOx NTE control area status")
	print("\t 7E\tPM NTE control area status")
	print("\t 7F\tEngine run time\n")
	
	print("\t 80\tPIDs supported [81-A0]")
	print("\t 81\tEngine run time for Auxiliary Emissions Control Device (AECD)")
	print("\t 82\tEngine run time for Auxiliary Emissions Control Device (AECD)")
	print("\t 83\tNOx sensor")
	print("\t 84\tManifold surface temperature")
	print("\t 85\tNOx reagent system")
	print("\t 86\tParticulate matter (PM) sensor")
	print("\t 87\tIntake manifold absolute pressure\n")
	
	print("\t A0\tPIDs supported [A1 - C0]\n")
	
	print("\t C0\tPIDs supported [C1 - E0]")
	print("\t C3\tReturns numerous data, including Drive Condition ID and Engine Speed*")
	print("\t C4\tB5 is Engine Idle Request. B6 is Engine Stop Request*\n")

	
	
def Menu02():
	print("Same as 01, but for the specified freeze frame")	
	
def Menu03():
	print("Requeset trouble codes")
	
def Menu04():
	print("Clear trouble codes / Malfunction Indicator lamp (MIL) / Check engine light")

def Menu05():
	print("PID \t\t Description")
	print("\t 0100\tOBD Monitor IDs supported [$01-$20]")
	print("\t 0101\tO2 Sensor Monitor Bank 1 Sensor 1")
	print("\t 0102\tO2 Sensor Monitor Bank 1 Sensor 2")
	print("\t 0103\tO2 Sensor Monitor Bank ")
	
def Menu06():
	print("PID \t\t Description")
	
def Menu07():
	print("PID \t\t Description")
	
def Menu08():
	print("PID \t\t Description")
	
def Menu09():
	print("PID \t\t Description")
	print("\t 00\tMode 9 Supported PIDs [01-20]")
	print("\t 01\tVIN Message Count in PID 02. Only for ISO 9141-2, ISO 14230-4, and SAE J1850")
	print("\t 02\tVehicle Identification Number (VIN)")
	print("\t 03\tCalibration ID message count for PID 04. Only for ISO 9141-2, ISO 14230-4 and SAE J1850")
	print("\t 04\tCalibration ID")
	print("\t 05\tCalibration verification numbers(CVN) message count for PID 06. Only for ISO 9141-2, ISO 14230-4 and SAE J1850")
	print("\t 06\tCalibration Verification Numbers (CVN)")
	print("\t 07\tIn-use performance tracking message count for PID 08 and 0B. Only for ISO 9141-2, ISO 14230-4 and SAE J1850")
	print("\t 08\tIn-use performance tracking for spark ignition vehicles")
	print("\t 09\tECU name message count for PID 0A")
	print("\t 0A\tECU name")
	print("\t 0B\tIn-use performance trackig for compression ignition vehicles")
	
def Menu0A():
	print("PID \t\t Description")
	

cont = 1
while(cont == 1):
	MainMenu()
	number = input("\nSelect a mode or select EXIT to exit program:\n")
	if (number == "01"):
		Menu01()
	
	elif (number == "02"):
		Menu02()
	
	elif (number == "03"):
		Menu03()
	
	elif (number == "04"):
		Menu04()
	
	elif (number == "05"):
		Menu05()
	
	elif (number == "06"):
		Menu06()
		
	elif (number == "07"):
		Menu07()
	
	elif (number == "08"):
		Menu08()
		
	elif (number == "09"):
		Menu09()
		
	elif (number == "0A"):
		Menu0A()
		
	elif (number == "EXIT"):
		cont = 0;
		
	else:
		print("Please use one of the specified codes.")
