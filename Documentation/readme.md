## Airkey Quick Start AT Commands
1. First you have to any serial software to send the AT commands. We are using XCOM tool to send the commands, this tool is also in Git repo you can download it.
   
   <img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/46af4a39-8185-4dea-981f-23146e019a35" />

   Change the language to Enlgish

2. Open the device manager to check the COMM PORT linked with the device
   
   <img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/6cb12908-c2ab-4516-b936-42cde012cf87" />

3. Open the "Datasheet_EWM" from this directory and check or test all the AT Commands
   
   <img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/d754230b-7007-46a0-a68e-65d2b6e15f0e" />

   <img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/b9860190-bc79-4e18-95c4-ff711f1d5b56" />
   

4. Check the AT Command as per below - select the COMM PORT and Baudrate - 115200

   <img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/a1b49e36-a654-435b-93f9-75e78fd21343" />


**5. UART AT Command Configuration**
   
   AT+HMODE=0 //Enter the configuration module

   <img width="480" height="480" alt="image" src="https://github.com/user-attachments/assets/6cea94fe-3aff-47d1-abc3-691a18679038" />

**6. TCP AT Command Configuration**
   
   - For this configuration Computer and the Airkey Hardware must be connected to the same WiFi network (2.4G). Once this is done open the "NetAssist" and open a TCP Server. You can change the port numbers, default is set to 8080

   <img width="5" height="480" alt="image" src="https://github.com/user-attachments/assets/4fd84793-9977-4128-91cb-dd92c7e0936c" />



     AT Command Configuration to connect to TCP Server
     
     AT+STA=MYWIFI,12345678         // set wifi account/password
     
     AT+CIPSTATE=10.48.114.128,8081  // Set the IP/port of the TCP server to connect to (as per NetAssist values)
     
     AT+HMODE=6                      // Enter mode 6, UART-TCP passthrough.

   <img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/aefc707c-542b-4dec-93c2-a2e926cdea8d" />

   - Once the TCP is connected. You can send and recieve the data

   <img width="1000" height="800" alt="image" src="https://github.com/user-attachments/assets/9e55c148-8d2b-4a5f-bf5d-72286bd3a1e4" />

   - You can also configure the module using AT commands using "NetAssist" by following these commands which allow to enter and exit the AT command mode using TCP

   Enter the following commands
     
     AT+AUTH=123456     // Perform permission verification to enter AT command mode

     AT                 // Verify entry into AT command mode

     AT+AUTHEXIT        // exit AT command configuration

   <img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/51681336-6c01-4bdd-8bb7-2de95642d8ae" />


**6. Lora Point to Point Commuication**

   Configure the Moudule 1 as below:
   
     AT+HMODE=0    // Enter configuration

     AT+TRANS=1    // Fixed-point transmission

     AT+ADDR=1     // Set module address to 00 01

     AT+CHANNEL=1  // set channel to 1

     AT+HMODE=1    // Set mode UART-LoRa pass-through, BLE listening Transmit/receive data in hexadecimal


   Configure the Moudule 2 as below:
   
     AT+HMODE=0    // Enter configuration

     AT+TRANS=1    // Fixed-point transmission

     AT+ADDR=2     // Set module address to 00 02

     AT+CHANNEL=1  // set channel to 1

     AT+HMODE=1    // Set mode UART-LoRa pass-through, BLE listening Transmit/receive data in hexadecimal

     00 01 01 AA BB CC   // Target address is 00 01, channel is 01, data is AA BB CC

   <img width="1000" height="700" alt="image" src="https://github.com/user-attachments/assets/e968d7c8-40ba-4013-bafc-b060b2c8ec9c" />
   

   <img width="1000" height="700" alt="image" src="https://github.com/user-attachments/assets/fe3d803b-3b39-4fc3-b7df-65f51fc5af2c" />




   




