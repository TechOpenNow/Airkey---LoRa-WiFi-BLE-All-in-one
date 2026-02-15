import airkey
import time

# Initialize the Serial Port with Comm Port
# ttyAMA0/ttyUSB0 for GPIO communication with Raspberry Pi
# COMx for PC 

device = airkey.module(port='COM4', baudrate=115200)    
device.open()

# Enter configuration mode 0
device.set_working_mode(0)
time.sleep(1)

# Set the LoRa transfer mode to FIXED
device.set_LORA_transfer_mode(1)
time.sleep(1)

# Set the module address to 1 (00 01)
device.set_LORA_module_address(2)
time.sleep(1)

# Set channle to 1
device.set_LORA_module_channel(1)
time.sleep(1)

# Enter configuration mode 1 - UART-LoRa pass-through, BLE listening
device.set_working_mode(1)
time.sleep(1)

# Target address is 00 01, channel is 01, data is AA BB CC
device.send_hex_data('00 01 01 AA BB CC')
time.sleep(1)

# Close the serial Communication
device.close()
    




