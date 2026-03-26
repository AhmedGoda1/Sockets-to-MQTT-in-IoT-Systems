import socket
import random
import time

SERVER_IP = "127.0.0.1" # I'm using a localhost since I have only this labtop and I missed this lecture in class

PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, PORT))
    print(f"Connected to server at {SERVER_IP}:{PORT}")

    while True:
        temperature = round(random.uniform(20, 35), 2)
        message = f"{temperature}"
        
        client.send(message.encode())
        print("Sensor value sent:", temperature)
        
        time.sleep(5)

except ConnectionRefusedError:
    print("Error: Could not connect. Is the server running?")
except KeyboardInterrupt:
    print("\nSensor stopping...")
finally:
    client.close()