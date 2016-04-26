
##########################
##   GENERAL COMMANDS   ##
##########################

# For more detail, visit page 11
# of the datasheet

# repeat the last command
REPEAT_CMD = ''

# Try Baud Rate Divisor hh
TRY_BAUD_DIVISOR = 'atbrd hh'

# Set Baud Rate Timeout
SET_BAUD_TIMEOUT = 'atbrt hh'

# Set all to Defaults
SET_ALL_DEFAULTS = 'atd'

# Echo off
ECHO_OFF = 'ate0'

# Echo on
ECHO_ON = 'ate1'

# Forget events
FORGET_EVNTS = 'atfe'

# Print version ID
PRINT_VRSN_ID = 'ati'

# Linefeeds off
LINEFEED_OFF = 'atl0'

# Linefeeds on
LINEFEED_ON = 'atl1'

# Enter low power mode
LOW_PWR = 'atlp'

# Memory off
MEM_OFF = 'atm0'

# Memory on
MEM_ON = 'atm1'

# Read stored data
READ_STORED_DATA = 'atrd'

# Save data byte hh
SAVE_DATA_BYTE = 'atsd hh'

# Warm start (quick reset)
WARM_START = 'atws'

# Reset all
RESET_ALL = 'atz'

# Display device description
DISP_DESC = 'at@1'

# Display device identifier
DISP_DEV_ID = 'at@2'

# Store device identifier
STORE_DEV_ID = 'at@3 cccccccccccc'



######################
##   OBD COMMANDS   ##
######################

# Allow long messages (>7 bytes)
ALLOW_LONG_MSGS = 'atal'

# Display activity monitor count 
ACTIVITY_MONITOR_COUNT = 'atamc'

# set the Activity Mon Timeout to hh
# replace hh with timeout period
ACTIVITY_MONITOR_TIMEOUT = 'atamt hh'

# Automatically Receive
AUTOMATIC_RECV = 'atar'

# Adaptive Timing off
ADAPTIVE_TIMING_OFF = 'atat0'

# Adaptive timing auto1
ADAPTIVE_TIMING_AUTO1 = 'atat1'

# Adaptive timing auto2
ADAPTIVE_TIMING_AUTO1 = 'atat2'

# Perform Buffer dunmp
BUFFER_DUMP = 'atbd'

# Bypass the Initialization sequence
BYP_INIT = 'atbi'

# Describe protocol
DESC_PROTOCOL = 'atdp'

# Describe the Protocol by Number
DESC_PROTOOOL_NUM = 'atdpn'

# headers off
HEADERS_OFF = 'ath0'

# headers on
HEADERS_ON = 'ath1'

# Monitor all
MONITOR_ALL = 'arma'

# Monitor for Receiver = hh
MONITOR_FOR_RECVR = 'atmr hh'

# Monitor for Transmitter = hh
MONITOR_FOR_TRANS = 'atmt hh'

# Normal Length messages*
NORMAL_LEN = 'atnl'

# Protocol close
PROTOCOL_CLOSE = 'atpc'

# Responses off
RESP_OFF = 'atr0'

# Response on
RESP_ON = 'atr1'

# Set the Receive Address to hh
SET_RECV_ADDR = 'atra hh'

######################
##   PRINT_SPACES   ##
######################

# Printing of spaces off
PRINT_SPACE_OFF = 'ats0'

# Printing of spaces on
PRINT_SPACE_ON = 'ats1'

######################
##   SET HEADER     ##
######################

# Set header to xyz
SET_HEADER_XYZ = 'atsh xyz'

# Set header to xxyyzz
SET_HEADER_XXYYZZ = 'atsh xxyyzz'

# Set header to wwxxyyzz
SET_HEADER_WWXXYYZZ = 'atsh wwxxyyzz'

######################
##   SET PROTOCOL   ##
######################

# Set Protocol to automatic
SET_PROTOCOL_AUTO = 'atsp 0'

# Set Protocol to SAE J1850 PWM (41.6 kbaud)
SET_PROTOCOL_J1850_PWM  = 'atsp 1'

# Set Protocol to SAE J1850 VPW (10.4 kbaud)
SET_PROTOCOL_J1850_VPW = 'atsp 2'

# Set Protocol to ISO 9141-2 (5 baud init, 10.4 kbaud)
SET_PROTOCOL_ISO_9141_2 = 'atsp 3'

# Set Protocol to ISO 14230-4 KWP (5 baud init, 10.4 kbaud)
SET_PROTOCOL_ISO_14230_4_KWP = 'atsp 4'

# Set Protocol to ISO 14230-4 KWP (fast init, 10.4 kbaud)
SET_PROTOCOL_ISO_4230_4_KWP_2 = 'atsp 5'

# Set Protocol to ISO 15765-4 CAN (11 bit ID, 500 kbaud)
SET_PROTOCOL_ISO_15765_4_CAN_11 = 'atsp 6'

# Set Protocol to ISO 15765-4 CAN (29 bit ID, 500 kbaud)
SET_PROTOCOL_ISO_15765_4_CAN_29 = 'atsp 7'

# Set Protocol to ISO 15765-4 CAN (11 bit ID, 250 kbaud) 
SET_PROTOCOL_ISO_15765_4_CAN_11 = 'atsp 8'

# Set Protocol to ISO_15765_4_CAN (29 bit ID, 250 kbaud)
SET_PROTOCOL_ISO_15765_4_CAN_29 = 'atsp 9'

# Set Protocol to SAE J1939 CAN (29 bit ID, 250* kbaud) 
SET_PROTOCOL_SAE_J1939_CAN = 'atsp a'

# Set Protocol to USER1 CAN (11* bit ID, 125* kbaud)
SET_PROTOCOL_USER1_CAN_125 = 'atsp b'

# Set Protocol to USER1 CAN (11* bit ID, 125* kbaud)
SET_PROTOCOL_USER1_CAN_50 = 'atsp c'


# Erase stored protocol
ERASE_PROTOCOL = 'atsp 00'

# Set the Receive address to hh
SET_RECV_ADDR = 'atsr hh'

# Use Standard Search order (J1978)
STANDARD_SEARCH = 'atss'

# Set Timeout to hh x 4 msec
SET_TIMEOUT = 'atst hh'