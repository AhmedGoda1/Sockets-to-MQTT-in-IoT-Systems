import paho.mqtt.client as mqtt
import random
import time

broker = "broker.emqx.io"
topic = "savonia/ahmedDaba/temperature"

client = mqtt.Client()
client.connect(broker, 1883)

print(f"Publisher started. Sending data to {topic}...")

try:
    while True:
        temperature = round(random.uniform(20, 35), 2)
        client.publish(topic, temperature)
        print("Published to MQTT:", temperature)
        time.sleep(5)
except KeyboardInterrupt:
    print("\nPublisher stopped.")
finally:
    client.disconnect()