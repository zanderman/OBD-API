/**
 * @file Accelerometer.ino
 *
 * Accelerometer configuration file
 */

#include <stdint.h>
#include <stdbool.h>
#define PART_TM4C123GH6PM
#define PART_TM4C1230C3PM

#include "driverlib/pin_map.h"
#include "inc/tm4c123gh6pm.h"
#include "driverlib/sysctl.h"
#include "inc/tm4c123gh6pm.h"
#include "inc/hw_i2c.h"
#include "inc/hw_memmap.h"
#include "inc/hw_types.h"
#include "inc/hw_gpio.h"
#include "driverlib/i2c.h"
#include "driverlib/sysctl.h"
#include "driverlib/gpio.h"
#include "driverlib/pin_map.h"

// Accelerometer Registers

#define DEV_ADDR           0x53

#define DEVID_REG          0x00
#define DEVID              0xE5

#define POWER_CTL          0x2D
#define MEASURE            0x08
#define STNDBY             0x00

#define BW_RATE            0x2C
#define INT_SOURCE         0x30

#define DATA_FORMAT        0x31
#define TWO_G              0x00
#define INT_INVERT         0x20
#define SIXTEEN_G          0x03

#define INT_ENABLE         0x2E
#define SINGLE_TAP         0x40
#define INACTIVITY         0X08

#define THRESH_TAP         0x1D
#define DUR                0x21

#define THRESH_INACT       0x25
#define TIME_INACT         0x26

#define ACT_INACT_CTL      0x27
#define INACT_AC_DC        0x00 // 0x00 = DC, 0x08 = AC
#define INACT_X_ENABLE     0x04
#define INACT_Y_ENABLE     0x02
#define INACT_Z_ENABLE     0x01
#define ACT_INACT_VAL      INACT_X_ENABLE | INACT_Y_ENABLE  // Enable x+y axis for inactivity

#define TAP_AXES     0x2A    
#define X_AXIS       0x04
#define Y_AXIS       0x02
#define Z_AXIS       0x01

#define DATAX0       0x32
#define DATAX1       0x33
#define DATAY0       0x34
#define DATAY1       0x35
#define DATAZ0       0x36
#define DATAZ1       0x37

void initI2C0(void);
bool initAccel(void);
uint8_t readI2C0(uint16_t device_address, uint16_t device_register);
void writeI2C0(uint16_t device_address, uint16_t device_register, uint8_t device_data);
void clearInterrupt(void);
void disableAccelInterrupts(void);

/**
 * Initialize the accelerometer
 * 
 * @return True if configured successfully
 */
bool initAccel()
{
  uint8_t i2c_data;
  bool success = false;
  
  #if defined VERBOSE
    Serial.println("AccelInit");
  #endif
  
  // Initialize I2C0
  initI2C0();
  
  // Read Device ID, check correctness
  i2c_data = readI2C0(DEV_ADDR, DEVID_REG);
  if(i2c_data == DEVID) success = true;
  
  // Set device in standby mode
  writeI2C0(DEV_ADDR, POWER_CTL, STNDBY); 
  i2c_data = readI2C0(DEV_ADDR, POWER_CTL);
  if(i2c_data != STNDBY) success = success && false;
  
  // Set Data Format to 2g, invert interrupt output
  writeI2C0(DEV_ADDR, DATA_FORMAT, TWO_G | INT_INVERT); 
  i2c_data = readI2C0(DEV_ADDR, DATA_FORMAT);
  if(i2c_data != (TWO_G | INT_INVERT)) success = success && false;
  
  // Configure and enable interrupt on INT1
  // Disable interrupts first
  writeI2C0(DEV_ADDR, INT_ENABLE, 0x00);
  i2c_data = readI2C0(DEV_ADDR, INT_ENABLE);
  if(i2c_data != 0x00) success = success && false;
  if(!success) Serial.println("INT_ENABLE");
  #if defined VERBOSE
    Serial.print("Int Enable: ");
    Serial.println(i2c_data, HEX);
  #endif
  
  // Setup tap threshold
  writeI2C0(DEV_ADDR, THRESH_TAP, THRESH_VAL);
  i2c_data = readI2C0(DEV_ADDR, THRESH_TAP);
  if(i2c_data != THRESH_VAL) success = success && false;
  #if defined VERBOSE
    Serial.print("THRESH TAP: ");
    Serial.println(i2c_data, HEX);
  #endif
  
  writeI2C0(DEV_ADDR, DUR, TAP_DUR_VAL);
  i2c_data = readI2C0(DEV_ADDR, DUR);
  if(i2c_data != TAP_DUR_VAL) success = success && false;
  #if defined VERBOSE
    Serial.print("DUR: ");
    Serial.println(i2c_data, HEX);
  #endif
  
  writeI2C0(DEV_ADDR, TAP_AXES, Z_AXIS);
  i2c_data = readI2C0(DEV_ADDR, TAP_AXES);
  if(i2c_data != Z_AXIS) success = success && false;
  #if defined VERBOSE
    Serial.print("TAP AXES: ");
    Serial.println(i2c_data, HEX);
  #endif
  
  writeI2C0(DEV_ADDR, INT_ENABLE, SINGLE_TAP);
  i2c_data = readI2C0(DEV_ADDR, INT_ENABLE);
  if(i2c_data != SINGLE_TAP) success = success && false;
  #if defined VERBOSE
    Serial.print("Int Enable: ");
    Serial.println(i2c_data, HEX);
  #endif
 
  // Begin measurement mode
  writeI2C0(DEV_ADDR, POWER_CTL, MEASURE);
  i2c_data = readI2C0(DEV_ADDR, POWER_CTL);
  if(i2c_data != MEASURE) success = success && false;
  
  // Clear interrupts
  readI2C0(DEV_ADDR, INT_SOURCE);
  
  return success;
}

/**
 * Clear accelerometer interrupts
 */
void clearInterrupt()
{
  // Read register to clear interrupts
  readI2C0(DEV_ADDR, INT_SOURCE);
}

/**
 * Disable Accelerometer Interrupts
 */
void disableAccelInterrupts()
{
  #if defined DEBUG
    Serial.println("\n Disabling Accel Interrupts\n");
  #endif
  
  uint8_t i2c_data;
  bool success = false;
  
  // Initialize I2C0
  initI2C0();
  
  // Read Device ID, check correctness
  i2c_data = readI2C0(DEV_ADDR, DEVID_REG);
  if(i2c_data == DEVID) success = true;
  
  // Set device in standby mode
  writeI2C0(DEV_ADDR, POWER_CTL, STNDBY); 
  i2c_data = readI2C0(DEV_ADDR, POWER_CTL);
  if(i2c_data != STNDBY) success = success && false;
  
  // Set Data Format to 2g
  writeI2C0(DEV_ADDR, DATA_FORMAT, TWO_G | INT_INVERT); 
  i2c_data = readI2C0(DEV_ADDR, DATA_FORMAT);
  if(i2c_data != TWO_G | INT_INVERT) success = success && false;
  
  // Configure and enable interrupt on INT1 for INACTIVITY
  // Disable interrupts first
  writeI2C0(DEV_ADDR, INT_ENABLE, 0x00);
  i2c_data = readI2C0(DEV_ADDR, INT_ENABLE);
  if(i2c_data != 0x00) success = success && false;
  #if defined VERBOSE
    Serial.print("Int Enable: ");
    Serial.println(i2c_data, HEX);
  #endif
  
  writeI2C0(DEV_ADDR, ACT_INACT_CTL, ACT_INACT_VAL);
  i2c_data = readI2C0(DEV_ADDR, ACT_INACT_CTL);
  if(i2c_data != ACT_INACT_VAL) success = success && false;
  #if defined VERBOSE
    Serial.print("ACT_INACT_CTL: ");
    Serial.println(i2c_data, HEX);
  #endif
 
  // Begin measurement mode
  writeI2C0(DEV_ADDR, POWER_CTL, MEASURE);
  i2c_data = readI2C0(DEV_ADDR, POWER_CTL);
  if(i2c_data != MEASURE) success = success && false;
  
  // Clear interrupts
  readI2C0(DEV_ADDR, INT_SOURCE);  
}

/**
 * Initialize the I2C Module
 */
void initI2C0(void)
{
	//enable I2C module
	SysCtlPeripheralEnable(SYSCTL_PERIPH_I2C0);

	//reset I2C module
	SysCtlPeripheralReset(SYSCTL_PERIPH_I2C0);

	//enable GPIO peripheral that contains I2C
	SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOB);

	// Configure the pin muxing for I2C0 functions on port B2 and B3.
  GPIOPinConfigure(GPIO_PB2_I2C0SCL);
	GPIOPinConfigure(GPIO_PB3_I2C0SDA);

	// Select the I2C function for these pins.
	GPIOPinTypeI2CSCL(GPIO_PORTB_BASE, GPIO_PIN_2);
	GPIOPinTypeI2C(GPIO_PORTB_BASE, GPIO_PIN_3);

	// Enable and initialize the I2C0 master module.  Use the system clock for
	// the I2C0 module.  The last parameter sets the I2C data transfer rate.
	// If false the data rate is set to 100kbps and if true the data rate will
	// be set to 400kbps.
	I2CMasterInitExpClk(I2C0_BASE, SysCtlClockGet(), false);

	//clear I2C FIFOs
	HWREG(I2C0_BASE + I2C_O_FIFOCTL) = 80008000;
}

/**
 * Get data from the I2C Bus
 * 
 * @param device_address The device address to read from
 * @param device_register The register to read from
 * @return Data read from device and register
 */
uint8_t readI2C0(uint16_t device_address, uint16_t device_register)
{
	//specify that we want to communicate to device address with an intended write to bus
	I2CMasterSlaveAddrSet(I2C0_BASE, device_address, false);

	//the register to be read
	I2CMasterDataPut(I2C0_BASE, device_register);

	//send control byte and register address byte to slave device
	I2CMasterControl(I2C0_BASE, I2C_MASTER_CMD_SINGLE_SEND);

	//wait for MCU to complete send transaction
	while(I2CMasterBusy(I2C0_BASE));

	//read from the specified slave device
	I2CMasterSlaveAddrSet(I2C0_BASE, device_address, true);

	//send control byte and read from the register from the MCU
	I2CMasterControl(I2C0_BASE, I2C_MASTER_CMD_SINGLE_RECEIVE);

	//wait while checking for MCU to complete the transaction
	while(I2CMasterBusy(I2C0_BASE));

	//Get the data from the MCU register and return to caller
	return( I2CMasterDataGet(I2C0_BASE));
}

/**
 * Write data to the device on I2C bus
 * 
 * @param device_address The device address to write data to
 * @param device_register The register to write data to
 * @param device_data The data to send to the device
 */
void writeI2C0(uint16_t device_address, uint16_t device_register, uint8_t device_data)
{
	//specify that we want to communicate to device address with an intended write to bus
	I2CMasterSlaveAddrSet(I2C0_BASE, device_address, false);

	//register to be read
	I2CMasterDataPut(I2C0_BASE, device_register);

	//send control byte and register address byte to slave device
	I2CMasterControl(I2C0_BASE, I2C_MASTER_CMD_BURST_SEND_START);

	//wait for MCU to finish transaction
	while(I2CMasterBusy(I2C0_BASE));

	//specify data to be written to the above mentioned device_register
	I2CMasterDataPut(I2C0_BASE, device_data);

	//wait while checking for MCU to complete the transaction
	I2CMasterControl(I2C0_BASE, I2C_MASTER_CMD_BURST_RECEIVE_FINISH);

	//wait for MCU & device to complete transaction
	while(I2CMasterBusy(I2C0_BASE));
}

/**@{*/


