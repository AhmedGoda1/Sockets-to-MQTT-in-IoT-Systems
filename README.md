# Lab Series: From Sockets to MQTT in IoT Systems

## Project Overview
This project simulates a complete IoT communication pipeline. 
It demonstrates how data moves from a physical environment (Sensor) to a local processing unit (Edge) and finally to a remote monitoring system (Cloud).

### System Architecture (Single-Device Simulation)
To simulate multiple devices on one machine, we use **Localhost (127.0.0.1)** for internal communication and a **Public MQTT Broker** for external communication.

1.  **Sensor Node**  Sends raw data via TCP Sockets.
2.  **Edge Device**  Acts as a Gateway, receiving socket data and forwarding it to the Cloud.
3.  **Cloud Server** Subscribes to the MQTT topic to display final data.

---
## SERVER_IP = "127.0.0.1" # I'm using a localhost since I have only this labtop and I missed this lecture in class

## Lab 1: Sensor to Edge (Socket Programming)

### Setup
* **Protocol:** TCP Sockets
* **IP Address:** `127.0.0.1` (Localhost)
* **Port:** `5000`

### Implementation
- `socket_server.py`: Listens for incoming sensor data.
- `socket_sensor.py`: Generates random temperature data and sends it to the server.

### Execution
1. Run the server: `python socket_server.py`
2. Run the sensor: `python socket_sensor.py`
![Socket Communication](<Screenshot 2026-03-26 105809.png>)

## Lab 2: Edge to Cloud (MQTT)

### Setup
* **Protocol:** MQTT (Publish/Subscribe)
* **Broker:** `broker.emqx.io` (Public)
* **Topic:** `savonia/iot/temperature` (or your unique topic)
![MQTT screenShot](<Screenshot 2026-03-26 110744.png>)
---

## Lab 3: Full IoT Pipeline (Integration)

### Final Architecture Flow
1. **Sensor (`socket_sensor.py`)** generates data → sends via **Socket** to Edge.
2. **Edge Device (`edge_device.py`)** receives data → forwards via **MQTT** to Cloud.
3. **Cloud Subscriber (`mqtt_subscriber.py`)** receives data from Broker → displays output.
![Full PipeLine](<Screenshot 2026-03-26 111420.png>)
### How to Run
To run the full simulation on one machine:
1. Open Terminal 1: `python mqtt_subscriber.py`
2. Open Terminal 2: `python edge_device.py`
3. Open Terminal 3: `python socket_sensor.py`

### Final Results
* **IP Addresses:** 127.0.0.1 (Localhost simulation as I don't have a second computer at the moment and I missed the lab in class)
* **Port:** 5000
* **MQTT Topic:** [Random temperature and I put my name besides it]

---

## Learning Outcomes
- Successfully implemented point-to-point TCP Socket communication.
- Implemented asynchronous messaging using the MQTT protocol.
- Developed an Edge Gateway to bridge local and cloud networks.