import paho.mqtt.client as mqtt

# Configuration
broker = "broker.emqx.io"

topic = "savonia/ahmedDaba/temperature" 

def on_message(client, userdata, msg):
    value = msg.payload.decode()
    print(f"Cloud received: {value}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")
    else:
        print(f"Failed to connect, return code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker...")
client.connect(broker, 1883)

# This keeps the program running to listen for messages
client.loop_forever()