# All about Library and example codes
This contains all the library related to Airkey boards and example codes to test the hardwares.

## Library Functions (airkey.py)

**Serial Communication Functions**

1. open - This function will open the serial communication as per the port, baudrate etc
2. send_data - Sends AT commands to serial port
3. receive_data - Recieve the data from serial port
4. parse_command - To parse AT commands
5. close - Close the serial communication

**Module Basic Commands Functions**

1. link_check - Test the Module by sending "AT" and wait for "AT_OK"
2. querry_MAC - Read the unique ID of the module
3. reset_module - This will software reset the module
4. factory_reset - Reset the module to default factory settings
5. set_working_mode - Set the communication modes (7 Modes)
6. read_working_mode - Read the current communcation mode

**WiFi/TCP Functions**

1. read_WIFI_STA - Read the SSID and password of the module WiFi
2. set_WIFI_STA - Set the SSID and password of the WiFi
3. read_TCP - Read the TCP server IP and PORT
4. set_TCP - Set the TCP server IP and PORT

**BLE Commands**
1. read_BLE_broadcast_name - Read the BLE name
2. set_BLE_broadcast_name - Set the BLE broadcast name no longer than 16 bytes
3. read_BLE_broadcast_interval - Read the BLE broadcast intervals. Interval value range 32-16384, default 1600, 1600*0.625ms=1000ms
4. set_BLE_broadcast_interval - Set the BLE broadcast intervals. Interval value range 32-16384, default 1600, 1600*0.625ms=1000ms
5. read_BLE_power - Read the BLE power levels (+20dbm to -9dbm range)
6. set_BLE_power - Set the BLE power levels (+20dbm to -9dbm range)

**LORA Functions**
1. read_LORA_airspeed - Read the LORA Airspeed (2.4K to 62.5K range)
2. set_LORA_airspeed - Set the LORA Airspeed (2.4K to 62.5K range)
3. read_LORA_packet_length - Read the LORA packet length
4. set_LORA_packet_length - Set the LORA packet length
5. read_LORA_transfer_mode - Read the transfer mode - Transparent or Fixed
6. set_LORA_transfer_mode - Set the transfer mode - Transparent or Fixed
7. read_LORA_relay_mode - Read the LORA relay mode status - ON or OFF
8. set_LORA_relay_mode - Set the LORA relay mode - ON or OFF
9. read_LORA_module_address - Read the LORA module address, Module address 0~65535 (decimal), default 0
10. set_LORA_module_address - Set the LORA module address, Module address 0~65535 (decimal), default 0
11. read_LORA_module_channel - Read the LORA module channel (0-83 range)
12. set_LORA_module_channel - Set the LORA module channel (0-83 range)
13. read_LORA_networkID - Read the LORA network ID (0 to 255 range)
14. set_LORA_networkID - Set the LORA network ID (0 to 255 range)
15. read_LORA_key - Read the LORA key, used for encryption (0 to 65535 range)
16. set_LORA_key - Set the LORA key, used for encryption (0 to 65535 range)

You can also create your functions in the library (airkey.py) as per the AT Commands

## Example Codes

**Example1_module_test** : This is basic AT test example code to check the link with module

**Example2_WIFI_TCP_Server** : In this example the module will be connected via WiFi to a TCP server and send the data to TCP server. Make sure your computer where TCP server is running using netassist will be on the same network as the module is connected to the WiFi using "set_WIFI_STA("MYWIFI", 12345678)"

Please follow the below steps:

1. Install the netassist.exe (check the tool directory to download). Run the netassist.exe and select TCP Server. Check the IP and Port (you can also change the port number), then update the same in this example code "set_TCP(your IP, your port)".

   <img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/543ae5a2-eacd-49ed-812d-2a795f7e67e1" />

2. You can also check the module datasheet for more information on this.

**Example_BLE_AT_Command**
Donwload the BLE tester App (https://play.google.com/store/apps/details?id=com.zhctwh.ble_tester) or you can use any other BLE apps.

Open the App -> Scan for devices (You will see ESM22Axxx)-> Go to Service FFF0 -> Select FFF3 Characteristic -> Change to ASCII and enable the Read - > send the AT+AUTH=123456, this is authorization key to enter to AT Commands -> You can test with AT command  

   <img width="1541" height="748" alt="image" src="https://github.com/user-attachments/assets/95284667-2210-4d17-9c7e-c8d19acd6cce" />




     


