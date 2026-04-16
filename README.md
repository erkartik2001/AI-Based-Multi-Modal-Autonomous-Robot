# AI-Based Multi-Modal Autonomous Robot (Distributed System)

## Overview

This project implements a distributed robotics system where perception, processing, and control are separated across multiple devices. A mobile device mounted on the robot streams video, a remote laptop performs computer vision and decision-making, and a NodeMCU (ESP8266) controls motors and sensors.

The system supports real-time object/person tracking, obstacle avoidance, and command-based navigation using WiFi communication.

---

## System Architecture

Mobile Camera → Laptop (CV + Decision) → NodeMCU → Motors & Sensors

- Mobile device streams video over WiFi
- Laptop processes frames using OpenCV
- Laptop sends commands over WiFi
- NodeMCU executes motor control and handles ultrasonic safety

---

## Features

- Real-time video streaming from mobile camera
- Computer vision-based tracking (face/object)
- Command generation (LEFT, RIGHT, FORWARD, STOP)
- WiFi-based communication between laptop and robot
- Obstacle detection using ultrasonic sensor
- Modular and scalable distributed architecture

---

## Technologies Used

- Python (OpenCV, Flask/Requests)
- Embedded C/C++ (Arduino IDE)
- WiFi Communication (ESP8266)
- IP Camera Streaming

---

## Project Structure

```
project-root/
│
├── hardware/
│ └── nodemcu_robot/
│ └── nodemcu_robot.ino
│
├── pc_python/
│ ├── camera_stream.py
│ ├── vision_processing.py
│ ├── command_sender.py
│ └── main.py
│
└── README.md
```

---

## File Descriptions

### hardware/nodemcu_robot/nodemcu_robot.ino
- Receives commands over WiFi
- Controls motors using L298N driver
- Reads ultrasonic sensor for obstacle avoidance
- Overrides unsafe commands

---

### pc_python/camera_stream.py
- Connects to mobile IP camera stream
- Captures frames using OpenCV

---

### pc_python/vision_processing.py
- Processes frames
- Performs detection (face/object)
- Determines robot direction

---

### pc_python/command_sender.py
- Sends commands to NodeMCU via HTTP or socket
- Handles communication layer

---

### pc_python/main.py
- Integrates all modules
- Runs main loop:
  - Capture frame
  - Process frame
  - Decide action
  - Send command

---

## Setup Instructions

### 1. Mobile Camera Setup
- Install IP Webcam / DroidCam
- Start video stream
- Note the streaming URL

---

### 2. Laptop Setup

Install dependencies:

pip install opencv-python requests flask numpy


Run: python main.py


---

### 3. NodeMCU Setup

- Flash Arduino code using Arduino IDE
- Connect NodeMCU to same WiFi network
- Note its IP address

---

## Communication Flow

1. Laptop fetches frames from mobile stream
2. Vision module processes frame
3. Decision logic determines movement
4. Command sent to NodeMCU over WiFi
5. NodeMCU controls motors accordingly

---

## Notes

- All devices must be on the same network (or use VPN)
- Avoid sending commands too frequently (reduce latency issues)
- Tune control logic for smoother movement

---

## Future Improvements

- Cloud-based communication for remote access
- Web dashboard for monitoring
- Advanced AI models for detection
- Gesture and voice integration

---

## License

This project is for academic and educational purposes.