# Airkey
AirKey is an open-source all-in-one wireless tool that combines BLE 5.0, Wi-Fi, and LoRa into a single, compact device. No more juggling multiple dongles or modules—AirKey gives you everything you need in one board. With USB and UART interface and ranges up to 500 m for BLE/Wi-Fi and 5 km for LoRa, AirKey is built for every makers and IoT innovators. Plus, features like remote configuration and relay networking make it easy to scale your projects without extra hardware.

Whether you choose the USB Dongle, the RP2040 module, or the Raspberry Pi HAT, AirKey delivers seamless connectivity and flexibility across all your workflows. 

All the Airkey boards comes with a LINK Indicator (Bluetooth/WIFI connection status)

BLE - Default high, BLE connected is low

WIFI - Default high, WIFI connected, TCP not connected outputs 1Hz high and low level change, TCP connected outputs low level

<img src="https://i.kickstarter.com/assets/051/028/828/d2938e267c89fac412611bec35e4f368_original.jpg?fit=scale-down&origin=ugc&q=92&v=1759140553&width=680&sig=Z%2FMNjh2UtI6iiaBT8%2FemkZhSqTBzUhm02250YQMpU7g%3D" alt="Airkey" width="50%"/>

## LoRa Features
- Multi Band support for different frequencies 433/868/915 Mhz
- Support AT commands and Hex Commands
- New generation LoRa spread spectrum modulation technology which brings longer communication distance and stronger anti-interference ability
- Support automatic relay networking, and multi-level relay is suitable for ultra-long-distance communication, and the same area runs multiple networks at the same time
- You can set your own communication key and encrypt the data
- Support RSSI signal strength indication function, which is used to evaluate signal quality, improve communication network, and range measurement
- Support wireless parameter configuration, sending command packets wirelessly to remotely configure or read wireless module parameters
- Supports Wake-on-Air
- Supports fixed-point transmission, broadcast transmission, and channel listening
- Supports data transmission rates from 2.4K to 62.5Kbps with range up to 5Km

## BLE Features
- Support the Bluetooth BLE 5.0 protocol
- Support Bluetooth parameter over-the-air configuration function
- Support transmit power modification with a maximum transmit power of 20dBm
- Maximum communication maximum distance up to 500m
- MTU max 517 byte

## WiFi Features
- Support STA working mode
- Supports disconnected automatic re-connection
- Supports WPA2 WIFI security authentication method
- Supports TCP CLIENT communication mode
- Transmit power is 20dBm
- Maximum communication distance up to 500m

## Airkey Raspberry Pi HAT - UART/USB Setting

<img width="380" height="380" alt="image" src="https://github.com/user-attachments/assets/fc0a444d-7cbe-47af-9a61-761960defca8" />

As you can see the Yellow Jumper, by changing these jumper settings you can change the UART/USB communication. Once the jumper is set to USB, then you can connect the USB cable to Airkey HAT and connect it with Raspberry Pi or to any other device and communicate.

## LoRa and WiFi Antenna

<img width="480" height="380" alt="image" src="https://github.com/user-attachments/assets/5a365296-8557-402d-a1e3-16785b04ff40" />

<img width="480" height="380" alt="image" src="https://github.com/user-attachments/assets/96a0a178-8e18-4172-af0b-71622659b990" />


The smaller antenna is of WiFi Antenna and Bigger Antenna is for LoRa

## Working Modes

[Documentation](Documentation/) - In this we have update complete examples of AT commands based testing and working of different modes without programming

[Software](Software/) - This contains all the libraries and software to work with Airkey. Airkey.py is differnt for RP2040 so please copy accordingly.

## Working Modes

Mode 1 

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/50e126c0-aef3-4c50-b108-04d50b2b26af" />

Mode 2

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/3da31781-1a3f-415a-b8c7-7f87078a42fe" />

Mode 3

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/93710e09-753a-4cf1-aecb-4dc57c088a24" />

Mode 4

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/68299f26-ff7e-4be7-bbae-2135432394c3" />

Mode 5

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/5208e81f-c3d5-4351-9c43-c584f0d8c6e7" />

Mode 6

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/6870ba64-9f85-4e38-b688-bb44e81c4e66" />

Mode 7

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/81295eb5-efc2-4510-92ba-e8ceb8d450ce" />



## USB Driver
- **CH340**: The hardware is based on the CH340 chip, incase of driver you can download it from the official website. You can download the drivers for windows/Mac/linux using the below link.
https://www.wch-ic.com/downloads/CH341SER_ZIP.html#carousel-example-generic

## Table of Contents
1. [Documentation](Documentation/) - This directory contains the datasheet of the module and AT commands instruction manual 
2. [Hardware](Hardware/) - This directory contains hardware STEP files
3. [Software](Software/) - This directory contains all the codes like library, example code and getting started
4. [Tools](Tools/) - This directory contains softwares used for testing the Airkey Boards like serial communication, netassist etc

  

