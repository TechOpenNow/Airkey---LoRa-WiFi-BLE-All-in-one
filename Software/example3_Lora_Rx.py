import airkey
import time

# Initialize the Serial Port with Comm Port
# ttyAMA0/ttyUSB0 for GPIO communication with Raspberry Pi
# COMx for PC 

device = airkey.module(port='COM14', baudrate=115200)    
device.open()

# Enter configuration mode 0
device.set_working_mode(0)
time.sleep(1)

# Set the LoRa transfer mode to FIXED
device.set_LORA_transfer_mode(1)
time.sleep(1)

# Set the module address to 1 (00 01)
device.set_LORA_module_address(1)
time.sleep(1)

# Set channle to 1
device.set_LORA_module_channel(1)
time.sleep(1)

# Enter configuration mode 1 - UART-LoRa pass-through, BLE listening
device.set_working_mode(1)
time.sleep(1)

# Transmit/Receive data in hexadecimal
while True:
    #print('Waiting for data..')
    lora_data = device.receive_hex_data()
    if(lora_data):
        print('LoRa Data Recieved:', lora_data)



