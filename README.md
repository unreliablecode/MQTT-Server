```markdown
# MQTT Communication Between Cloud VPS and ESP32

This project demonstrates how to set up MQTT communication between an ESP32 running MicroPython and a Python-based MQTT server hosted on a cloud VPS. The server can receive sensor data from the ESP32 and send control commands back to it.

## Overview

The project consists of two main components:
1. **Server**: A Python MQTT server running on a cloud VPS using the `paho-mqtt` library.
2. **ESP32**: An ESP32 device running MicroPython, using the `umqtt.simple` library to communicate with the server.

### Features
- **Two-way communication**: The ESP32 publishes sensor data, and the server can send control commands (like turning an LED on or off) to the ESP32.
- **MQTT protocol**: Reliable, lightweight messaging protocol ideal for IoT applications.

## Repository Structure
- `server.py`: Contains the Python server code that runs on your cloud VPS.
- `main.py`: Contains the MicroPython code that runs on your ESP32.

## How to Use

### 1. Set Up the Server (Cloud VPS)
1. Install Python and the required libraries:
   ```bash
   pip install paho-mqtt
   ```
2. Update the MQTT broker IP in `server.py` to match your VPS IP or domain.
3. Run the server:
   ```bash
   python server.py
   ```

### 2. Set Up the ESP32 (Client)
1. Flash MicroPython firmware onto your ESP32.
2. Upload `main.py` to the ESP32 using a tool like `ampy` or `rshell`.
3. Update the WiFi credentials and MQTT broker IP in `main.py` to match your network and VPS.
4. Connect the ESP32 to WiFi and run the script.

### MQTT Topics
- **Subscribe (ESP32 -> Server)**: `esp32/sensor`  
  The ESP32 publishes sensor data to this topic.
  
- **Publish (Server -> ESP32)**: `esp32/control`  
  The server can send control commands (e.g., to turn an LED on/off) using this topic.

## Requirements
- Python 3.x (for the server)
- MicroPython (for the ESP32)
- `paho-mqtt` library (server-side)
- `umqtt.simple` library (ESP32-side)

## Author
Created by [unreliablecode](https://github.com/unreliablecode).
```

This `README.md` gives an overview without including the actual code and directs users to the appropriate files (`server.py` and `main.py`).
