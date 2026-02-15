import airkey

# Initialize the Serial Port with Comm Port
device = airkey.module()    
device.open()

# Check the link with using by sending AT command
device.link_check()

# Check the MAC Address
device.querry_MAC()



