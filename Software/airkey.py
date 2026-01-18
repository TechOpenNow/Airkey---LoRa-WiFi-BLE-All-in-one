import serial
import time

class LoraMesh:
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initializes the serial communication settings for AT commands.
        
        :param port: COM port or device ('/dev/ttyUSB0' on Linux)
        :param baudrate: Baud rate for the communication (default: 115200)
        :param timeout: Timeout in seconds for reading from the serial port (default: 1 second)
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None
        self.info = None
    
    def open(self):
        """Opens the serial connection."""
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            print(f"Connected to {self.port} at {self.baudrate} baud.")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
    
    def send_data(self, command, wait_for_response=True, delay=0.5):
        """
        Sends an AT command to the serial port and optionally waits for a response.
        
        :param command: The AT command to send (string)
        :param wait_for_response: Flag to wait for response after sending the command (default: True)
        :param delay: Delay before reading the response (default: 1 second)
        :return: The response received from the device, or None if no response is received
        """
        if self.ser and self.ser.is_open:
            # Send the AT command with a carriage return (CR) at the end
            # command = f"{command}\r"
            self.ser.write(command.encode())
            print(f"\nSent: {command.strip()}")
            
            if wait_for_response:
                time.sleep(delay)  # Wait for the response
                response = self.receive_data()
                return response
        else:
            print("Serial port is not open.")
            return None
    
    def receive_data(self, size=256):
        """
        Reads data from the serial port.
        
        :param size: Number of bytes to read (default: 256 bytes)
        :return: Data received as bytes
        """
        if self.ser and self.ser.is_open:
            data = self.ser.readall()
            if data:
                print(f"Received: {data.decode(errors='ignore')}", end="")
            else:
                print("No data received.")
            return data.decode(errors='ignore')
        else:
            print("Serial port is not open.")
            return ""
    
    def parse_command(command):
        """Parase AT Command"""
        print("Data = " + param)
        param = command.strip().split('=')
    
        if len(param) > 0:
            return param
        else:
            return False
    
    def close(self):
        """Closes the serial connection."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"Connection to {self.port} closed.")
        else:
            print("Serial port is not open.")
    
    # ======================== Module Basic Commands ============================
            
    def link_check(self):
        """
        Test the Module with AT Command
        
        @Return:
        Success (True) or Failure (False)
        """
        command = "AT"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"\nInfo - Moudle is connected")
            return(True)
        else:
            print(f"\nError - Module not connected..!")
            return(False)
        
    
    def querry_MAC(self):
        """
        Read the Unique ID of the module (MAC Address)
        
        @Return:
        MAC Address or False
        """
        command = "AT+UID=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - MAC Address is : {param[0]}")
        return(param[0])
    

    def reset_module(self):
        """
        This command will reset the modue
        
        @Return:
        
        """
        command = "AT+RESET"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        print(f"\nInfo - Moudle Software RESET Done")
        
    def factory_reset(self):
        """
        Reset to module to factory default settings
        
        @Return:
        
        """
        command = "AT+DEFAULT"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('_')
        print(f"\nInfo - Factory Reset Done")

    # ----------------------------------------------------------------------------------------
    # ============================ Working Mode - Read/Write ============================
    def set_working_mode(self, mode=0):
        """
        Set the communication mode of the module
        
        @Parameters 
        mode: Seven Modes
        0 - Configuration Mode
        1 - UART/LORA pass-through, BLE listening
        2 - UART/BLE pass-through, LORA listening
        3 - LORA/BLE pass-through, UART listening
        4 - UART/LORA pass-through, WIFI listening
        5 - UART/WIFI pass-through, LORA listening
        6 - LORA/WIFI pass-through, UART listening
        7 - LORA/UART pass-through, WIFI/BLE both OFF

        @Return:
        Success (True) or Failure (False)
        """
        command = f"AT+HMODE={mode};"
        response = self.send_data(command, wait_for_response=True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK\r'):
            print(f"Info - Communication Working Mode is set to : {mode}")
            return(True)
        else:
            print(f"Error - Working Mode not set")
            return(False)

    def read_working_mode(self):
        """
        Read the Communication Mode
        
        @Return -
        Mode Number: Seven Modes
        0 - Configuration Mode
        1 - UART/LORA pass-through, BLE listening
        2 - UART/BLE pass-through, LORA listening
        3 - LORA/BLE pass-through, UART listening
        4 - UART/LORA pass-through, WIFI listening
        5 - UART/WIFI pass-through, LORA listening
        6 - LORA/WIFI pass-through, UART listening
        7 - LORA/UART pass-through, WIFI/BLE both OFF
        """
        command = 'AT+HMODE=?'
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[0] == '0\r'):
            print(f"Info - Mode : 0 - Configuration Mode")
            return(0)
        elif(param[0] == '1\r'):
            print(f"Info - Mode : 1 - UART/LORA pass-through, BLE listening")
            return(1)
        elif(param[0] == '2\r'):
            print(f"Info - Mode : 2 - UART/BLE pass-through, LORA listening")
            return(2)
        elif(param[0] == '3\r'):
            print(f"Info - Mode : 3 - LORA/BLE pass-through, UART listening")
            return(3)
        elif(param[0] == '4\r'):
            print(f"Info - Mode : 4 - UART/LORA pass-through, WIFI listening")
            return(4)
        elif(param[0] == '5\r'):
            print(f"Info - Mode : 5 - UART/WIFI pass-through, LORA listening")
            return(5)
        elif(param[0] == '6\r'):
            print(f"Info - Mode : 6 - LORA/WIFI pass-through, UART listening")
            return(6)
        elif(param[0] == '7\r'):
            print(f"Info - Mode : 7 - LORA/UART pass-through, WIFI/BLE both OFF")
            return(7)
        else:
            print(f"Error - Communication Mode Read")
            return(False)
    # ----------------------------------------------------------------------------------------
    
    # ================================ WiFi/TCP Commands ===================================
    def read_WIFI_STA(self):
        """
        Read the WiFi: name and password

        @Return
        SSID,PASSWORD
        """
        command = "AT+STA=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - SSID & Password : {param[0]}")
        return(param[0])
        
        
    def set_WIFI_STA(self, ssid, password):
        """
        Set the WiFi and Password

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+STA={ssid},{password}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - WiFi STA set to : {ssid},{password}")
            return(True)
        else:
            print(f"Error - WiFi STA setting")
            return(False)
        
    def read_TCP(self):
        """
        Read the TCP Server: IP and Port

        @Return
        IP, Port
        """
        command = "AT+CIPSTATE=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - TCP (IP & Port) : {param[0]}")
        return(param[0])
    
    def set_TCP(self, IP, port):
        """
        Set the TCP - IP and port
        Only IPV4 IP addresses are supported.

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+CIPSTATE={IP},{port}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - TCP set to : {IP},{port}")
            return(True)
        else:
            print(f"Error - TCP setting")
            return(False)
    
    # ----------------------------------------------------------------------------------------
    # ================================ BLE Commands =========================================
    def read_BLE_broadcast_name(self):
        """
        Read the BLE Broadcast Name

        @Return
        BLE Name
        """
        command = "AT+BLENAME=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - BLE broadcast name : {param[0]}")
        return(param[0])
    
    def set_BLE_broadcast_name(self, name):
        """
        Set the BLE broadcast name
        Broadcast name length no greater than 16 bytes

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+BLENAME={name}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - BLE broadcast name set to : {name}")
            return(True)
        else:
            print(f"Error - BLE broadcast name not set")
            return(False)
        
    def read_BLE_broadcast_interval(self):
        """
        Read the BLE Broadcast intervals
        Interval value range 32-16384, default 1600, 1600*0.625ms=1000ms

        @Return
        BLE interval
        """
        command = "AT+BLEADV=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - BLE broadcast interval : {param[0]}")
        return(param[0])
    
    def set_BLE_broadcast_interval(self, interval):
        """
        Set the BLE broadcast interval
        Interval value range 32-16384, default 1600, 1600*0.625ms=1000ms

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+BLEADV={interval}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - BLE broadcast interval set to : {interval} ({interval * 0.625}ms)")
            return(True)
        else:
            print(f"Error - BLE broadcast name not set")
            return(False)
        
    def read_BLE_power(self):
        """
        Read the BLE power levels
        0 --- +20dbm
        1 --- +15dbm
        2 --- +9dbm
        3 --- +3dbm
        4 --- 0dbm(default)
        5 --- -3dbm
        6 --- -9dbm

        @Return
        BLE power level
        """
        command = "AT+BLEPOWER=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - BLE power level : {param[0]}")
        return(param[0])
    
    def set_BLE_power(self, level):
        """
        Set the BLE power levels
        0 --- +20dbm
        1 --- +15dbm
        2 --- +9dbm
        3 --- +3dbm
        4 --- 0dbm(default)
        5 --- -3dbm
        6 --- -9dbm

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+BLEPOWER={level}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - BLE power level set to : {level}")
            return(True)
        else:
            print(f"Error - BLE power level")
            return(False)
        
    # ----------------------------------------------------------------------------------------
    # ================================ LORA Commands =========================================
    def read_LORA_airspeed(self):
        """
        Read the LORA Airspeed
        Value ranges:
        0 --- 2.4K
        1 --- 2.4K
        2 --- 2.4K
        3 --- 4.8K
        4 --- 9.6K
        5 --- 19.2K
        6 --- 38.4K
        7 --- 62.5K

        @Return
        LORA airspeed
        """
        command = "AT+RATE=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA airspeed is : {param[0]}")
        return(param[0])

    def set_LORA_airspeed(self, value):
        """
        Set the LORA airspeed
        Value ranges:
        0 --- 2.4K
        1 --- 2.4K
        2 --- 2.4K
        3 --- 4.8K
        4 --- 9.6K
        5 --- 19.2K
        6 --- 38.4K
        7 --- 62.5K

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+RATE={value}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA airspeed set to : {value}")
            return(True)
        else:
            print(f"Error - LORA airspeed setting")
            return(False)
    
    def read_LORA_packet_length(self):
        """
        Read the LORA packet length
        Value ranges:
        0 --- 240 (default)
        1 --- 128
        2 --- 64
        3 --- 32

        @Return
        LORA packet length
        """
        command = "AT+PACKET=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA packet length is : {param[0]}")
        return(param[0])
    
    def set_LORA_packet_length(self, value):
        """
        Set the LORA packet length
        Value ranges:
        0 --- 240 (default)
        1 --- 128
        2 --- 64
        3 --- 32

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+PACKET={value}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA packet length set to : {value}")
            return(True)
        else:
            print(f"Error - LORA packet length setting")
            return(False)
        
    def read_LORA_transfer_mode(self):
        """
        Read the LORA transfer mode - Transparent or Fixed point
        Value ranges:
        0 --- Transparent (default)
        1 --- Fixed point

        @Return
        LORA transfer mode
        """
        command = "AT+TRANS=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA transfer mode : {param[0]}")
        return(param[0])
    
    def set_LORA_transfer_mode(self, mode):
        """
        Set the LORA transfer mode
        Value ranges:
        0 --- Transparent (default)
        1 --- Fixed

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+TRANS={mode}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA transfer mode set : {mode}")
            return(True)
        else:
            print(f"Error - LORA transfer mode setting")
            return(False)
        
    def read_LORA_relay_mode(self):
        """
        Read the LORA relay mode - ON or OFF
        Value ranges:
        0 --- OFF (default)
        1 --- ON

        @Return
        LORA relay mode
        """
        command = "AT+ROUTER=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA relay mode : {param[0]}")
        return(param[0])
    
    def set_LORA_relay_mode(self, mode):
        """
        Set the LORA relay mode - ON or OFF
        Value ranges:
        0 --- OFF (default)
        1 --- ON

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+ROUTER={mode}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA relay mode set : {mode}")
            return(True)
        else:
            print(f"Error - LORA relay mode setting")
            return(False)
        
    def read_LORA_module_address(self):
        """
        Read the LORA module address
        Module address 0~65535 (decimal), default 0

        @Return
        LORA module address
        """
        command = "AT+ADDR=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA module address : {param[0]}")
        return(param[0])
    
    def set_LORA_module_address(self, address):
        """
        Set the LORA module address
        Module address 0~65535 (decimal), default 0

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+ADDR={address}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA module address : {address}")
            return(True)
        else:
            print(f"Error - LORA module address setting")
            return(False)
        
    def read_LORA_module_channel(self):
        """
        Read the LORA module channel
        0-83 represent a total of 84 channels (for 400 band) respectively
        0-80 represent a total of 81 channels respectively (for 900 band)
        
        Actual frequency = 410.125 + CHANNEL * 1M
        Actual frequency = 850.125 + CHANNEL * 1M

        @Return
        LORA module channel
        """
        command = "AT+CHANNEL=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA module channel : {param[0]}")
        return(param[0])
    
    def set_LORA_module_channel(self, channel):
        """
        Set the LORA module channel
        0-83 represent a total of 84 channels (for 400 band) respectively
        0-80 represent a total of 81 channels respectively (for 900 band)
        
        Actual frequency = 410.125 + CHANNEL * 1M
        Actual frequency = 850.125 + CHANNEL * 1M

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+CHANNEL={channel}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA module channel : {channel}")
            return(True)
        else:
            print(f"Error - LORA module channel setting")
            return(False)
        
    def read_LORA_networkID(self):
        """
        Read the LORA network ID
        Module network 0~255 (decimal), default 0

        @Return
        LORA network ID
        """
        command = "AT+NETID=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA network ID : {param[0]}")
        return(param[0])
    
    def set_LORA_networkID(self, ID):
        """
        Set the LORA network ID
        Module network 0~255 (decimal), default 0

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+NETID={ID}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA network ID : {ID}")
            return(True)
        else:
            print(f"Error - LORA network ID setting")
            return(False)
        
    def read_LORA_key(self):
        """
        Read the LORA Key
        Module key 0~65535 (decimal),default 0
        
        Used for encryption to avoid interception of over-the-air wireless data by similar modules;
        The module will internally use these two bytes as a calculation factor to transform and encrypt
        the over-the-air wireless signal

        @Return
        LORA Key
        """
        command = "AT+KEY=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')
        
        print(f"Info - LORA Key : {param[0]}")
        return(param[0])
    
    def set_LORA_key(self, key):
        """
        Set the LORA Key
        Module key 0~65535 (decimal),default 0
        
        Used for encryption to avoid interception of over-the-air wireless data by similar modules;
        The module will internally use these two bytes as a calculation factor to transform and encrypt
        the over-the-air wireless signal

        @Return
        Success (True) or Failure (False)
        """
        command = f"AT+KEY={key}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('\n')

        if(param[1] == 'AT_OK'):
            print(f"Info - LORA Key : {key}")
            return(True)
        else:
            print(f"Error - LORA key setting")
            return(False)
        




    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    # ================================ Read Module Info ===================================
    def read_module_info(self):
        """
        Read the module parameteres

        @Return
        Module all Info paramters
        """
        response = self.send_data('AT+INFO=?', wait_for_response = True)
        return(response)
    # ----------------------------------------------------------------------------------------

    # ================== Destination Address - Read/Write ===================================
    def set_destination_addr(self, address=0, flash=0):
        """
        Set the Destination address
        
        @Parameters
        address: It can be 0 ~ 65535
        flash: 0 (don't save in flash) or 1 (save in flash)
        
        @Return
        Success (True) or Failure (False)
        """ 
        command = f"AT+DST_ADDR={address},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Destination address set to : {address}")
            return(True)
        else:
            print(f"Error - Destination address")
            return(False)

    def read_destination_addr(self):
        """
        Read the Destination address
        
        @Return
        Address or False
        """
        command = 'AT+DST_ADDR=?'
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
        print(f"Info - Destination Address is : {param[1]}")
        return(param[1])
    # ----------------------------------------------------------------------------------------

    # ============================ Communication Mode - Read/Write ============================
    def set_comm_mode(self, mode=3, flash=0):
        """
        Set the communication mode of the module
        
        @Parameters 
        mode: Four Modes (1 : Unicast),(2 : Multicast),(3 : Broadcast),(4 : Anycast)
        flash = 0 (Don't save in flash), 1 (Save in flash)

        @Return:
        Success (True) or Failure (False)
        """
        command = f"AT+OPTION={mode},{flash};"
        response = self.send_data(command, wait_for_response=True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Source address is set to : {mode}")
            return(True)
        else:
            print(f"Error - Source address")
            return(False)

    def read_comm_mode(self):
        """
        Read the Communication Mode
        
        Return -
        Mode - (1 : Unicast),(2 : Multicast),(3 : Broadcast),(4 : Anycast)
        """
        command = 'AT+OPTION=?'
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        if(param[1] == '1'):
            print(f"Info - Communication Mode is : 1 - Unicast")
            return(param[1])
        elif(param[1] == '2'):
            print(f"Info - Communication Mode is : 2 - Multicast")
            return(param[1])
        elif(param[1] == '3'):
            print(f"Info - Communication Mode is : 3 - Broadcast")
            return(param[1])
        elif(param[1] == '4'):
            print(f"Info - Communication Mode is : 4 - Anycast")
            return(param[1])
        else:
            print(f"Error - Communication Mode Read")
            return(False)
    # ----------------------------------------------------------------------------------------

    # ======================== Source Address - Read/Write ====================================
    def set_source_addr(self, address=0, flash=0):
        """
        Set the source address
        
        @Parameters
        address: It can be 0 ~ 65535
        flash: 0 (don't save in flash) or 1 (save in flash)
        
        @Return
        Success (True) or Failure (False)
        """ 
        command = f"AT+SRC_ADDR={address},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Source address set to : {address}")
            return(True)
        else:
            print(f"Error - Source address")
            return(False)

    def read_source_addr(self):
        """
        Read the source address
        
        @Return
        Address 
        """
        command = 'AT+SRC_ADDR=?'
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
        print(f"Info - Source Address is : {param[1]}")
        return(param[1])
    # -----------------------------------------------------------------------------------------

    # ========================= Send Data to Other LoraMesh Devices ========================
    def send_LORA_data(self, dataToSend, ):
        """
        Send the data to other LoraMesh devices
        
        @Return:
        
        """
        #self.ser.write(dataToSend.encode())
        
        response = self.send_data(dataToSend, wait_for_response = True, delay=2)
        return(response)
        '''
        if(response == "SUCCESS\r\n"):
            print(f"Data Sent : {response}")
            return(True)
        else:
            print(f"ERROR - Data sent - {response}")
            return(response)
        '''
        
    # ----------------------------------------------------------------------------------------

    # ==================================== Module RESET ======================================
    def reset_module(self):
        """
        Reset the LORA Mesh Module
        
        @Return:
        Success (True) or Failure (False)
        """
        command = "AT+RESET"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"\nInfo - Module Reset Done")
            return(True)
        else:
            print(f"\nError - Module Reset")
            return(False)
    # ----------------------------------------------------------------------------------------

    # ================================ Default Factory Settings =================================
    def reset_Factory(self):
        """
        Reset the Lora to factory settings
        
        @Return:
        Success (True) or Failure (False)
        """
        command = "AT+DEFAULT"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"\nInfo - Factory Reset Done")
            return(True)
        else:
            print(f"\nError - Factory Reset")
            return(False)
      
    # ----------------------------------------------------------------------------------------

    # ================================ Read MAC Address =================================
    def read_MAC_address(self):
        """
        Read the unique 32 bit address of the MCU of the LORA Module
        
        @Return:
        Address
        """
        command = "AT+MAC=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
        print(f"Info - MAC Address is : {param[0]}")
        return(param[0])
        
    # ----------------------------------------------------------------------------------------

    # ================================ Type of Node (Routing / Terminal)=================================
    def read_node_type(self):
        """
        Read the type of the Node - Terminal or Routing
        
        @Return:
        Node Type
        """
        command = "AT+TYPE=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        if(param[1] == '0'):
            print(f"Info - Node Type (0) - Routing Node")
            return(param[1])
        elif(param[1] == '1'):
            print(f"Info - Node Type (1) - Terminal Node")
            return(param[1])
        else:
            print(f"Error - Node type")
    # ---------------------------------------------------------------------------------------------

    # ================================ RF Output Power (Read/Write)=================================
    def read_RF_power(self):
        """
        Read the type of the Node - Terminal or Routing
        
        @Return:
        Address or Failure (False)
        """
        command = "AT+POWER=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        print(f"Info - RF Power is : {param[1]}")
        return(param[1])
        
    def set_RF_power(self, power=0, flash=0):
        """
        Read the type of the Node - Terminal or Routing
        
        @Return:
        Address or Failure (False)
        """
        command = f"AT+POWER={power},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - RF power set to : {power}")
            return(True)
        else:
            print(f"Error - RF power")
            return(False)
    # ---------------------------------------------------------------------------------------------

    # ============================ Frequency band/channel (Read/Write)==========================
    def read_freq_channel(self):
        """
        Read the frequency band
        E52-400NW22S frequency band: RF working channel (0 ~ 99)
        E52-900NW22S frequency band: RF working channel (0 ~ 79)
        
        @Return:
        Channel or Failure (False)
        """
        command = "AT+CHANNEL=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        print(f"Info - Frequency Channel : {param[1]}")
        return(param[1])
        
    def set_freq_channel(self, channel=0, flash=0):
        """
        Write the frequency channel
        
        @Parameters
        channel: E52-400NW22S frequency band: RF working channel (0 ~ 99)
                 E52-900NW22S frequency band: RF working channel (0 ~ 79)
        flash: 0 (Don't save to flash) or 1 (save to flash)

        @Return:
        Success (True) or Failure (False)
        """
        command = f"AT+CHANNEL={channel},{flash};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Frequency channel set to : {channel}")
            return(True)
        else:
            print(f"Error - Frequency channel")
            return(False)
    # ---------------------------------------------------------------------------------------------

    # ============================ Air Data Rate (Read/Write) ==================================
    def read_air_rate(self):
        """
        Read the air data rate
        (0 - 62.5K),(1 - 21.825K), (2 - 7K)
        
        @Return:
        Rate Value or Failure (False)
        """
        command = "AT+RATE=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')
    
        if(param[1] == '0'):
            print(f"Info - Air Data Rate (0) - 62.5K")
            return(param[0])
        elif(param[1] == '1'):
            print(f"Info - Air Data Rate (1) - 21.825K")
            return(param[0])
        elif(param[1] == '2'):
            print(f"Info - Air Data Rate (2) - 7K")
            return(param[0])
        else:
            print(f"Error - Read air data rate")
            return(False)
        
    def set_air_rate(self, rate=0):
        """
        Write the air data rate

        @Parameters
        rate: Use values (0 - 62.5K),(1 - 21.825K), (2 - 7K)

        """
        command = f"AT+RATE={rate}"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Air data rate set to : {rate}")
            return(True)
        else:
            print(f"Error - Air data rate")
            return(False)
    # --------------------------------------------------------------------------------------------

    # ================================ Frame Header (Enable/Disable) =============================
    def read_frame_header(self):
        """
        Read status of the data frame header
        
        @Return:
        Enable = 1 and Disable = 0
        """
        command = "AT+HEAD=?"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')
        param = param[1].split(',')

        print(f"Info - Frame Header status : {param[1]}")
        return(param[1])
        
    def set_frame_header(self, enable = 1):
        """
        Set the frame header packet enable/disable

        @Parameters
        enable: 1 for Enable and 0 for Disable
        flash: 0 (Don't save to flash) or 1 (save to flash)
        """
        command = f"AT+HEAD={enable};"
        response = self.send_data(command, wait_for_response = True)
        param = response.strip().split('=')

        if(param[1] == 'OK'):
            print(f"Info - Frame Header is : {enable}")
            return(True)
        else:
            print(f"Error - Air data rate")
            return(False)

