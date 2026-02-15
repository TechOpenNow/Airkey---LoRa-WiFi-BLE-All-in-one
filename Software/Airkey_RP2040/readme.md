
# All about Airkey_RP2040 Library and example codes
This contains all the library related to Airkey RP2040 board and example codes to test the hardwares.

## Library Functions (airkey.py)

**Serial Communication Functions**

1. open - Initializes UART communication for RP2040. UART number (0), TX pin - GP0, RX pin - GP1, Baudrate 115200
2. send_data - Sends AT commands to serial port
3. send_hex_data - Send the data in HEX format, example to send data on LoRa HEX is needed
4. receive_data - Recieve the data from serial port
5. receive_hex_data - Recieve the data in HEX format
6. parse_command - To parse AT commands

Rest all the functions in the RP2040 library are same as previous airkey library.

**Start with Thoony**

 - Connect the Airkey_RP2040 with the computer
 - Open the Thonny IDE and select the MicroPython Raspberry Pi Pico
 - Copy the airkey.py library to the baord
 - copy the example code and paste to main.py and run the code

<img width="700" height="600" alt="image" src="https://github.com/user-attachments/assets/7660ceea-37a4-4f74-bce5-5e5ed92844e5" />

