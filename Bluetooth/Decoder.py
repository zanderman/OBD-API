import scanner
from obd import OBD

BAUD = 115200
B01_20 = 0
B21_40 = 0
B41_60 = 0
B61_80 = 0
B81_A0 = 0
BA1_C0 = 0
BC1_E0 = 0

def setup():
	adapters = scanner.scan("OBD")
	if len( adapters ) == 0:
		print "[!]\tNo adapters were found that have 'OBD' in their name.\nExiting..."
	else:
		global adapter
		adapter = OBD( type="bluetooth", addr=adapters[0]['addr'], name=adapters[0]['name'], baud=BAUD )
		adapter.bind()
		adapter.connect()
		print(SendOBD("ate0"))
		print(SendOBD("atl0"))
		print(SendOBD("ath0"))

def getTimeSinceEngineStart():
	tses = SendOBD("011F")
	tses = tses.split()
	a = int(tses[2], 16)
	b = int(tses[3], 16)
	return ((a * 256) + b)
	
def getDistTraveledWithMIL():
	dtwm = SendOBD("0121")
	dtwm = dtwm.split()
	a = int(dtwm[2], 16)
	b = int(dtwm[3], 16)
	return ((a * 256) + b)

def getNumberofWarmupsSinceCodesCleared():
	nwscc = SendOBD("0130")
	nwscc = nwscc.split()
	return int(nwscc[2], 16)

def getDistTraveledSinceCodesCleared():
	dtscc = SendOBD("0131")
	dtscc = dtscc.split()
	a = int(dtscc[2], 16)
	b = int(dtscc[3], 16)
	return ((a * 256) + b)

def getTimeRunWithMIL():
	trwm = SendOBD("014D")
	trwm = trwm.split()
	a = int(trwm[2], 16)
	b = int(trwm[3], 16)
	return ((a * 256) + b)

def getTimeSinceTroubleCodesCleared():
	tstcc = SendOBD("014E")
	tstcc = tstcc.split()
	a = int(tstcc[2], 16)
	b = int(tstcc[3], 16)
	return ((a * 256) + b)

def getRPM():
	rpm = SendOBD("010C")
	rpm = rpm.split()
	rpm = rpm[2] + rpm[3]
	return ((int(rpm, 16)) / 4)

def getSpeed():
	speed = SendOBD("010D")
	speed = speed.split()
	speed = speed[2]
	return (int(speed, 16))

def getControlModuleVoltage():
	cmv = SendOBD("0142")
	cmv = cmv.split()
	a = int(cmv[2], 16)
	b = int(cmv[3], 16)
	return (((a*256)+b)/1000)

def getVIN():
	vin = SendOBD("0902")
	spl = vin.split()
	#spl2 = spl[5:7]+ spl[9:15]+ spl[17:23]
	spl.remove('014')
	spl.remove('0:')
	spl.remove('02')
	spl.remove('01')
	spl.remove('1:')
	spl.remove('2:')
	del spl[0]
	spl2 = spl
	vin = ""
	for i in range (0, len(spl2)):
		#for j in range(0, len(spl2[i])):
		vin = vin + spl2[i]
	vin = vin.decode("hex")
	return vin


def functEnDis(code):
	answer = SendOBD(code)
	if (answer == "NO DATA"):
		return "0"
	else:
		spl = answer.split()
		resp = ""
		for i in range(2, len(spl)):
			resp = resp + spl[i]
		return resp

def SendOBD(code):
	print("Sending OBDII CODE: " + str(code))
	# send OBDII CODE
	adapter.send(code)
	rec = adapter.receive()
	return rec

def MenuFxCheck():
	# send 0100 to check 01-20
	global B01_20
	# assign B01_20 accordingly
	B01_20 = int(functEnDis("0100"), 16)
	# send 0120 to check 21-40
	# assign B21_40 accordingly
	global B21_40
	B21_40 = int(functEnDis("0120"), 16)
	# send 0140 to check 41-60
	# assign B41_60 accordingly
	global B41_60
	B41_60 = int(functEnDis("0140"), 16)
	# send 0160 to check 61-80
	# assign B61_80 accordingly
	global B61_80
	B61_80 = int(functEnDis("0160"), 16)
	# send 0180 to check 81-A0
	# assign B81_A0 accordingly
	global B81_A0
	B81_A0 = int(functEnDis("0180"), 16)
	# send 01A0 to check A1-C0
	# assign BA1_C0 accordingly
	global BA1_C0
	BA1_C0 = int(functEnDis("01A0"), 16)
	# send 01C1 to check C1-E0
	# assign BC1_E0 accordingly
	global BC1_E0
	BC1_E0 = int(functEnDis("01C0"), 16)
	
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
	menu = ("PID \t\t Description") + "\n"
	menu = menu +("\t 00\tPIDs supported [01 - 20]") + "\n"
	if (B01_20 & 0x80000000):
		menu = menu +("\t 01\tMonitor status since DTCs cleared") + "\n"
	if (B01_20 & 0x40000000):
		menu = menu +("\t 02\tFreeze DTC") + "\n"
	if (B01_20 & 0x20000000):
		menu = menu +("\t 03\tFuel system status") + "\n"
	if (B01_20 & 0x10000000):
		menu = menu +("\t 04\tCalculated engine load value") + "\n"
	if (B01_20 & 0x08000000):
		menu = menu +("\t 05\tEngine coolant temperature") + "\n"
	if (B01_20 & 0x04000000):
		menu = menu +("\t 06\tShort term fuel % trim-Bank 1") + "\n"
	if (B01_20 & 0x02000000):
		menu = menu +("\t 07\tLong term fuel % trim-Bank 1") + "\n"
	if (B01_20 & 0x01000000):
		menu = menu +("\t 08\tShort term fuel % trim-Bank 2") + "\n"
	if (B01_20 & 0x00800000):
		menu = menu +("\t 09\tLong term fuel % trim-Bank 2") + "\n"
	if (B01_20 & 0x00400000):
		menu = menu +("\t 0A\tFuel pressure") + "\n"
	if (B01_20 & 0x00200000):
		menu = menu +("\t 0B\tIntake manifold absolute pressure") + "\n"
	if (B01_20 & 0x00100000):
		menu = menu +("\t 0C\tEngine RPM") + "\n"
	if (B01_20 & 0x00080000):
		menu = menu +("\t 0D\tVehicle speed") + "\n"
	if (B01_20 & 0x00040000):
		menu = menu +("\t 0E\tTiming advance") + "\n"
	if (B01_20 & 0x00020000):
		menu = menu +("\t 0F\tIntake air temperature") + "\n"
	menu = menu +("\n\n")
	
	if (B01_20 & 0x00010000):
		menu = menu +("\t 10\tMAF air flow rate") + "\n"
	if (B01_20 & 0x00008000):
		menu = menu +("\t 11\tThrottle position") + "\n"
	if (B01_20 & 0x00004000):
		menu = menu +("\t 12\tCommanded Secondary air status") + "\n"
	if (B01_20 & 0x00002000):
		menu = menu +("\t 13\tOxygen sensors present") + "\n"
	if (B01_20 & 0x00001000):
		menu = menu +("\t 14\tBank 1, Sensor 1: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000800):
		menu = menu +("\t 15\tBank 1, Sensor 2: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000400):
		menu = menu +("\t 16\tBank 1, Sensor 3: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000200):
		menu = menu +("\t 17\tBank 1, Sensor 4: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000100):
		menu = menu +("\t 18\tBank 2, Sensor 1: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000080):
		menu = menu +("\t 19\tBank 2, Sensor 2: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000040):
		menu = menu +("\t 1A\tBank 2, Sensor 3: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000020):
		menu = menu +("\t 1B\tBank 2, Sensor 4: Oxygen sensor Voltage, Short term fuel trim") + "\n"
	if (B01_20 & 0x00000010):
		menu = menu +("\t 1C\tOBD standards this vehicle conforms to") + "\n"
	if (B01_20 & 0x00000008):
		menu = menu +("\t 1D\tOxygen sensors present") + "\n"
	if (B01_20 & 0x00000004):
		menu = menu +("\t 1E\tAuxiliary input status") + "\n"
	if (B01_20 & 0x00000002):
		menu = menu +("\t 1F\tRun time since engine start") + "\n"
	menu = menu +("\n\n")
	
	if (B01_20 & 0x00000001):
		menu = menu +("\t 20\tPIDs supported [21 - 40]") + "\n"
	if (B21_40 & 0x80000000):
		menu = menu +("\t 21\tDistance traveled with malfunction indicator lamp (MIL) on") + "\n"
	if (B21_40 & 0x40000000):
		menu = menu +("\t 22\tFuel rail Pressure (relative to manifold vacuum)") + "\n"
	if (B21_40 & 0x20000000):
		menu = menu +("\t 23\tFuel rail Pressure (diesel, or gasoline direct inject)") + "\n"
	if (B21_40 & 0x10000000):
		menu = menu +("\t 24\tO2S1_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x08000000):
		menu = menu +("\t 25\tO2S2_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x04000000):
		menu = menu +("\t 26\tO2S3_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x02000000):
		menu = menu +("\t 27\tO2S4_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x01000000):
		menu = menu +("\t 28\tO2S5_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x00800000):
		menu = menu +("\t 29\tO2S6_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x00400000):
		menu = menu +("\t 2A\tO2S7_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x00200000):
		menu = menu +("\t 2B\tO2S8_WR_lambda(1): Equivalence Ratio Voltage") + "\n"
	if (B21_40 & 0x00100000):
		menu = menu +("\t 2C\tCommanded EGR") + "\n"
	if (B21_40 & 0x00080000):
		menu = menu +("\t 2D\tEGR Error") + "\n"
	if (B21_40 & 0x00040000):
		menu = menu +("\t 2E\tCommanded evaporative purge") + "\n"
	if (B21_40 & 0x00020000):
		menu = menu +("\t 2F\tFuel Level Input") + "\n"
	menu = menu +("\n\n")
	
	if (B21_40 & 0x00010000):
		menu = menu +("\t 30\t# of warm-ups since codes cleared") + "\n"
	if (B21_40 & 0x00008000):
		menu = menu +("\t 31\tDistance traveled since codes cleared") + "\n"
	if (B21_40 & 0x00004000):
		menu = menu +("\t 32\tEvap. System Vapor Pressure") + "\n"
	if (B21_40 & 0x00002000):
		menu = menu +("\t 33\tBarometric pressure") + "\n"
	if (B21_40 & 0x00001000):
		menu = menu +("\t 34\t02S1_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000800):
		menu = menu +("\t 35\t02S2_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000400):
		menu = menu +("\t 36\t02S3_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000200):
		menu = menu +("\t 37\t02S4_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000100):
		menu = menu +("\t 38\t02S5_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000080):
		menu = menu +("\t 39\t02S6_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000040):
		menu = menu +("\t 3A\t02S7_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000020):
		menu = menu +("\t 3B\t02S8_WR_lambda(1) Equivalence Ratio Current") + "\n"
	if (B21_40 & 0x00000010):
		menu = menu +("\t 3C\tCatalyst Temperature Bank 1, Sensor 1") + "\n"
	if (B21_40 & 0x00000008):
		menu = menu +("\t 3D\tCatalyst Temperature Bank 2, Sensor 1") + "\n"
	if (B21_40 & 0x00000004):
		menu = menu +("\t 3E\tCatalyst Temperature Bank 1, Sensor 2") + "\n"
	if (B21_40 & 0x00000002):
		menu = menu +("\t 3F\tCatalyst Temperature Bank 2, Sensor 2") + "\n"
	menu = menu +("\n\n")
	
	if (B21_40 & 0x00000001):
		menu = menu +("\t 40\tPIDs Supported [41 - 60]") + "\n"
	if (B41_60 & 0x80000000):
		menu = menu +("\t 41\tMonitor status this drive cycle") + "\n"
	if (B41_60 & 0x40000000):
		menu = menu +("\t 42\tControl module voltage") + "\n"
	if (B41_60 & 0x20000000):
		menu = menu +("\t 43\tAbsolute load value") + "\n"
	if (B41_60 & 0x10000000):
		menu = menu +("\t 44\tFuel / Air commanded equivalence ratio") + "\n"
	if (B41_60 & 0x08000000):
		menu = menu +("\t 45\tRelative throttle position") + "\n"
	if (B41_60 & 0x04000000):
		menu = menu +("\t 46\tAmbient air temperature") + "\n"
	if (B41_60 & 0x02000000):
		menu = menu +("\t 47\tAbsolute throttle position B") + "\n"
	if (B41_60 & 0x01000000):
		menu = menu +("\t 48\tAbsolute throttle position C") + "\n"
	if (B41_60 & 0x00800000):
		menu = menu +("\t 49\tAccelerator pedal position D") + "\n"
	if (B41_60 & 0x00400000):
		menu = menu +("\t 4A\tAccelerator pedal position E") + "\n"
	if (B41_60 & 0x00200000):
		menu = menu +("\t 4B\tAccelerator pedal position F") + "\n"
	if (B41_60 & 0x00100000):
		menu = menu +("\t 4C\tCommanded throttle actuator") + "\n"
	if (B41_60 & 0x00080000):
		menu = menu +("\t 4D\tTime run with MIL on") + "\n"
	if (B41_60 & 0x00040000):
		menu = menu +("\t 4E\tTime since trouble codes cleared") + "\n"
	if (B41_60 & 0x00020000):
		menu = menu +("\t 4F\tMaximum value for equivalence ratio, oxygen sensor voltage, oxygen sensor current, and intake manifold absolute pressure") + "\n"
	menu = menu +("\n")
	
	if (B41_60 & 0x00010000):
		menu = menu +("\t 50\tMaximum value for air flow rate from mass air flow sensor") + "\n"
	if (B41_60 & 0x00008000):
		menu = menu +("\t 51\tFuel Type") + "\n"
	if (B41_60 & 0x00004000):
		menu = menu +("\t 52\tEthanol fuel %") + "\n"
	if (B41_60 & 0x00002000):
		menu = menu +("\t 53\tAbsolute Evap System Vapor Pressure") + "\n"
	if (B41_60 & 0x00001000):
		menu = menu +("\t 54\tEvap system vapor pressure") + "\n"
	if (B41_60 & 0x00000800):
		menu = menu +("\t 55\tShort term secondary oxygen sensor trim bank 1 and bank 3") + "\n"
	if (B41_60 & 0x00000400):
		menu = menu +("\t 56\tLong term secondary oxygen sensor trim bank 1 and bank 3") + "\n"
	if (B41_60 & 0x00000200):
		menu = menu +("\t 57\tShort term secondary oxygen sensor trim bank 2 and bank 4") + "\n"
	if (B41_60 & 0x00000100):
		menu = menu +("\t 58\tLong term secondary oxygen sensor trim bank 2 and bank 4") + "\n"
	if (B41_60 & 0x00000080):
		menu = menu +("\t 59\tFuel rail pressure (absolute)") + "\n"
	if (B41_60 & 0x00000040):
		menu = menu +("\t 5A\tRelative accelerator pedal position") + "\n"
	if (B41_60 & 0x00000020):
		menu = menu +("\t 5B\tHybrid battery pack remaining life") + "\n"
	if (B41_60 & 0x00000010):
		menu = menu +("\t 5C\tEngine oil temperature") + "\n"
	if (B41_60 & 0x00000008):
		menu = menu +("\t 5D\tFuel injection timing") + "\n"
	if (B41_60 & 0x00000004):
		menu = menu +("\t 5E\tEngine fuel rate") + "\n"
	if (B41_60 & 0x00000002):
		menu = menu +("\t 5F\tEmission requirements to which vehicle is designed") + "\n"
	menu = menu +("\n\n")
	
	if (B41_60 & 0x00000001):
		menu = menu +("\t 60\tPIDs supported [61-80]") + "\n"
	if (B61_80 & 0x80000000):
		menu = menu +("\t 61\tDriver's demand engine - percent torque") + "\n"
	if (B61_80 & 0x40000000):
		menu = menu +("\t 62\tActual engine - percent torque") + "\n"
	if (B61_80 & 0x20000000):
		menu = menu +("\t 63\tEngine reference torque") + "\n"
	if (B61_80 & 0x10000000):
		menu = menu +("\t 64\tEngine percent torque data") + "\n"
	if (B61_80 & 0x08000000):
		menu = menu +("\t 65\tAuxiliary input / output supported") + "\n"
	if (B61_80 & 0x04000000):
		menu = menu +("\t 66\tMass air flow sensor") + "\n"
	if (B61_80 & 0x02000000):
		menu = menu +("\t 67\tEngine coolant temperature") + "\n"
	if (B61_80 & 0x01000000):
		menu = menu +("\t 68\tIntake air temperature sensor") + "\n"
	if (B61_80 & 0x00800000):
		menu = menu +("\t 69\tCommanded EGR and EGR Error") + "\n"
	if (B61_80 & 0x00400000):
		menu = menu +("\t 6A\tCommanded Diesel intake air flow control and relative intake air flow position") + "\n"
	if (B61_80 & 0x00200000):
		menu = menu +("\t 6B\tExhaust gas recirculation temperature") + "\n"
	if (B61_80 & 0x00100000):
		menu = menu +("\t 6C\tCommanded throttle actuator control and relative throttle position") + "\n"
	if (B61_80 & 0x00080000):
		menu = menu +("\t 6D\tFuel pressure control system") + "\n"
	if (B61_80 & 0x00040000):
		menu = menu +("\t 6E\tInjection pressure control system") + "\n"
	if (B61_80 & 0x00020000):
		menu = menu +("\t 6F\tTurbocharger compressor inlet pressure") + "\n"
	menu = menu +("\n\n")
	
	if (B61_80 & 0x00010000):
		menu = menu +("\t 70\tBoost pressure control") + "\n"
	if (B61_80 & 0x00008000):
		menu = menu +("\t 71\tVariable Geometry turbo (VGT) control") + "\n"
	if (B61_80 & 0x00004000):
		menu = menu +("\t 72\tWastegate control") + "\n"
	if (B61_80 & 0x00002000):
		menu = menu +("\t 73\tExhaust pressure") + "\n"
	if (B61_80 & 0x00001000):
		menu = menu +("\t 74\tTurbocharger RPM") + "\n"
	if (B61_80 & 0x00000800):
		menu = menu +("\t 75\tTurbocharger temperature") + "\n"
	if (B61_80 & 0x00000400):
		menu = menu +("\t 76\tTurbocharger temperature") + "\n"
	if (B61_80 & 0x00000200):
		menu = menu +("\t 77\tCharge air cooler temperature (CACT)") + "\n"
	if (B61_80 & 0x00000100):
		menu = menu +("\t 78\tExhaust Gas temperature (EGT) Bank 1") + "\n"
	if (B61_80 & 0x00000080):
		menu = menu +("\t 79\tExhaust Gas temperature (EGT) Bank 2") + "\n"
	if (B61_80 & 0x00000040):
		menu = menu +("\t 7A\tDiesel particulate filter (DPF)") + "\n"
	if (B61_80 & 0x00000020):
		menu = menu +("\t 7B\tDiesel particulate filter (DPF)") + "\n"
	if (B61_80 & 0x00000010):
		menu = menu +("\t 7C\tDiesel Particulate filter (DPF) temperature") + "\n"
	if (B61_80 & 0x00000008):
		menu = menu +("\t 7D\tNOx NTE control area status") + "\n"
	if (B61_80 & 0x00000004):
		menu = menu +("\t 7E\tPM NTE control area status") + "\n"
	if (B61_80 & 0x00000002):
		menu = menu +("\t 7F\tEngine run time") + "\n"
	menu = menu +("\n\n")
	
	if (B61_80 & 0x00000001):
		menu = menu +("\t 80\tPIDs supported [81-A0]") + "\n"
	if (B81_A0 & 0x80000000):
		menu = menu +("\t 81\tEngine run time for Auxiliary Emissions Control Device (AECD)") + "\n"
	if (B81_A0 & 0x40000000):
		menu = menu +("\t 82\tEngine run time for Auxiliary Emissions Control Device (AECD)") + "\n"
	if (B81_A0 & 0x20000000):
		menu = menu +("\t 83\tNOx sensor") + "\n"
	if (B81_A0 & 0x10000000):
		menu = menu +("\t 84\tManifold surface temperature") + "\n"
	if (B81_A0 & 0x08000000):
		menu = menu +("\t 85\tNOx reagent system") + "\n"
	if (B81_A0 & 0x04000000):
		menu = menu +("\t 86\tParticulate matter (PM) sensor") + "\n"
	if (B81_A0 & 0x02000000):
		menu = menu +("\t 87\tIntake manifold absolute pressure") + "\n"
		menu = menu +("\n\n")
	
	if (B81_A0 & 0x00000001):
		menu = menu +("\t A0\tPIDs supported [A1 - C0]") + "\n"
		menu = menu +("\n\n")
	
	if (BA1_C0 & 0x00000001):
		menu = menu +("\t C0\tPIDs supported [C1 - E0]") + "\n"
	if (BC1_E0 & 0x20000000):
		menu = menu +("\t C3\tReturns numerous data, including Drive Condition ID and Engine Speed*") + "\n"
	if (BC1_E0 & 0x10000000):
		menu = menu +("\t C4\tB5 is Engine Idle Request. B6 is Engine Stop Request*") + "\n"
		menu = menu +("\n")
	return menu
	
	
def Menu02():
	return ("Same as 01, but for the specified freeze frame")	
	
def Menu03():
	return ("Requeset trouble codes")
	
def Menu04():
	return ("Clear trouble codes / Malfunction Indicator lamp (MIL) / Check engine light")

def Menu05():
	menu = ("PID \t\t Description") + ("\t 0100\tOBD Monitor IDs supported [$01-$20]") + ("\t 0101\tO2 Sensor Monitor Bank 1 Sensor 1") + ("\t 0102\tO2 Sensor Monitor Bank 1 Sensor 2") + ("\t 0103\tO2 Sensor Monitor Bank ")
	return menu
	
def Menu06():
	return ("PID \t\t Description")
	
def Menu07():
	return ("PID \t\t Description")
	
def Menu08():
	return ("PID \t\t Description")
	
def Menu09():
	menu = ""
	menu = "PID \t\t Description" + ("\n\t 00\tMode 9 Supported PIDs [01-20]") + ("\n\t 01\tVIN Message Count in PID 02. Only for ISO 9141-2, ISO 14230-4, and SAE J1850") + ("\n\t 02\tVehicle Identification Number (VIN)") + ("\n\t 03\tCalibration ID message count for PID 04. Only for ISO 9141-2, ISO 14230-4 and SAE J1850") + ("\n\t 04\tCalibration ID") + ("\n\t 05\tCalibration verification numbers(CVN) message count for PID 06. Only for ISO 9141-2, ISO 14230-4 and SAE J1850") + ("\n\t 06\tCalibration Verification Numbers (CVN)") + ("\n\t 07\tIn-use performance tracking message count for PID 08 and 0B. Only for ISO 9141-2, ISO 14230-4 and SAE J1850") + ("\n\t 08\tIn-use performance tracking for spark ignition vehicles") + ("\n\t 09\tECU name message count for PID 0A") + ("\n\t 0A\tECU name") + ("\n\t 0B\tIn-use performance trackig for compression ignition vehicles")
	return menu
	
def Menu0A():
	return ("PID \t\t Description")
	
