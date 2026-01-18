import airkey

# Initialize the Serial Port with Comm Port
# ttyAMA0 for GPIO communication with Raspberry Pi
# ttyUSB0 for USB with Raspberry Pi
# COMx for PC 

device = airkey.module(port='COM14', baudrate=115200)    
device.open()

# Check the link with using by sending AT command
device.link_check()

# Close the serial port
device.close()

