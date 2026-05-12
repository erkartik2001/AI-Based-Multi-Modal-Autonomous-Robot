# AI-Based Distributed Teleoperation Robot System

## Overview

This project implements a distributed robotic teleoperation system where video streaming, processing, and robot control are separated across multiple devices.

A mobile phone mounted on the robot acts as an RTSP camera server, a laptop acts as the control station and processing unit, and a NodeMCU (ESP8266) controls motors and sensors.

The system currently focuses on low-latency manual teleoperation using live RTSP video streaming and WiFi-based robot control.

---

# Current System Flow

Phone Camera (RTSP Stream)
        ↓
Python Control Station (GUI + Video Feed)
        ↓
ESP8266 NodeMCU
        ↓
Motor Driver (L298N)
        ↓
DC Motors

---

## Why Computer Vision Is Currently Disabled

Initial testing with OpenCV-based autonomous navigation introduced significant latency because:

- RTSP video decoding already consumes processing time
- Additional computer vision processing increased frame delay
- Command response became slow and unstable for realtime navigation
- Network latency + CV inference caused delayed robot reactions

For stable teleoperation and smoother control, the system currently uses:

- Live RTSP video feed
- Manual GUI-based controls
- ESP-side ultrasonic obstacle override

The architecture still supports future AI/CV integration.

---

## Features

- Live RTSP video streaming from mobile phone
- GUI-based robot control station
- Forward / Backward / Left / Right / Stop controls
- Dynamic speed control
- WiFi-based robot communication
- Ultrasonic obstacle detection on ESP8266
- Safety override for close obstacles
- Distributed robotics architecture
- Modular software structure

---

## Technologies Used

### Python Side
- OpenCV
- Tkinter GUI
- Requests
- Pillow (PIL)
- FFmpeg backend for RTSP

### Embedded Side
- ESP8266 NodeMCU
- Arduino IDE
- Embedded C/C++

### Communication
- RTSP video streaming
- HTTP-based robot commands over WiFi

---

## Hardware Components

- ESP8266 NodeMCU
- L298N Motor Driver
- DC Gear Motors
- Ultrasonic Sensor (HC-SR04)
- Li-ion Battery Pack
- Android Mobile Phone (RTSP Camera)

---

## Project Structure

```
project-root/
│
├── hardware/
│   └── nodemcu_robot/
│       └── nodemcu_robot.ino
│
├── pc_python/
│   ├── main.py
│   ├── rtsp_stream.py
│   ├── robot_controller.py
└── README.md
````

---

# File Descriptions

## hardware/nodemcu_robot/nodemcu_robot.ino

Responsibilities:

* Receives movement commands over WiFi
* Controls motors using L298N
* Handles PWM speed control
* Reads ultrasonic sensor
* Overrides dangerous movement commands
* Prevents collisions

---

## pc_python/robot_gui.py

Main control station GUI.

Responsibilities:

* RTSP stream display
* Robot IP connection
* Directional control buttons
* Speed controls
* Connect/disconnect handling

---

## pc_python/rtsp_stream.py

Responsibilities:

* Connects to RTSP stream
* Fetches frames using OpenCV + FFmpeg
* Handles stream resizing and rendering

---

## pc_python/robot_controller.py

Responsibilities:

* Sends HTTP requests to ESP8266
* Handles movement commands
* Controls robot speed

---

# Setup Instructions

## 1. Phone RTSP Camera Setup

Install an RTSP camera server app on Android.

Recommended:

* RTSP Camera Server
* Larix Broadcaster

Start RTSP server and note URL.

Example: **rtsp://192.168.1.4:1945/**

---

# 2. ESP8266 Setup

Flash the NodeMCU code using Arduino IDE.

Connect:

* Motors via L298N
* Ultrasonic sensor
* Battery pack

After boot:

* Connect ESP8266 to WiFi
* Note local IP printed in Serial Monitor

Example:**192.168.1.13**

---

# 3. Python Environment Setup

Install required modules: **pip install opencv-python pillow requests numpy**


Linux users may also need: **sudo apt install ffmpeg**


---

# 4. Running the System

Run the GUI application: **python robot_gui.py**


---

# GUI Usage

## Add RTSP URL

Example: **rtsp://192.168.1.4:1945/**

Click: **Start Stream**

The live camera feed will appear inside the GUI.

---

## Add ESP8266 IP

Example: **192.168.1.13**

Click: **Connect Robot**

---

## Robot Controls

Buttons:

* FORWARD
* BACKWARD
* LEFT
* RIGHT
* STOP

Speed:

* Speed +
* Speed -

Disconnect:

* Disconnect All

---

# Communication Flow

## Video Flow


Phone RTSP Stream
        ↓
Python OpenCV Capture
        ↓
GUI Display


---

## Control Flow


GUI Button Click
        ↓
Python HTTP Request
        ↓
ESP8266 Receives Command
        ↓
Motor Control

---

# Network Requirements

Currently:

* All devices must be connected to the same WiFi/hotspot network

This includes:

* Phone camera
* Laptop
* ESP8266

---

# Power Notes

* High motor speed can cause ESP8266 brownout/reboots
* PWM speed limits are recommended
* Capacitors near ESP power input improve stability
* Long/thin wires can introduce voltage drops and noise

---

# Current Limitations

* CV-based autonomous navigation disabled due to latency
* RTSP stream depends on local network stability
* L298N driver introduces voltage loss
* High-resolution streams increase delay

---

# Future Improvements

* MQTT-based cloud communication
* Web dashboard
* WASD keyboard controls
* Joystick support
* Video recording
* Battery monitoring
* AI object detection
* Autonomous/manual mode switching
* ROS integration
* GStreamer low-latency pipeline
* WebRTC support
* SLAM and mapping
* Multi-camera support

---

# Engineering Concepts Demonstrated

* Distributed robotics systems
* RTSP streaming
* Embedded motor control
* PWM speed control
* WiFi communication
* Event-driven GUI systems
* Ultrasonic obstacle avoidance
* Edge robotics architecture

---
