import socket
import paho.mqtt.client as mqtt

# Socket Config
HOST = "0.0.0.0"
PORT = 5000

# MQTT Config
broker = "broker.emqx.io"
topic = "savonia/ahmedDaba/temperature"

# 1. Setup MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.connect(broker, 1883)
print("Connected to MQTT Broker (Cloud)")

# 2. Setup Socket Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Edge device waiting for sensor...")
conn, addr = server.accept()
print("Sensor connected via socket:", addr)

try:
    while True:
        # Receive from Socket
        data = conn.recv(1024)
        if not data:
            break
        
        value = data.decode()
        print(f"Edge received from Sensor: {value}")

        # Forward to MQTT
        mqtt_client.publish(topic, value)
        print(f"Forwarded to Cloud via MQTT: {value}")

except KeyboardInterrupt:
    print("\nEdge device stopping...")
finally:
    conn.close()
    server.close()
    mqtt_client.disconnect()