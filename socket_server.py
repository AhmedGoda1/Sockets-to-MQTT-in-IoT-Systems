import socket

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server started. Listening on port {PORT}...")
print("Waiting for sensor connection...")

conn, addr = server.accept()
print("Connected by:", addr)

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Sensor data received:", data.decode())
except KeyboardInterrupt:
    print("\nServer stopping...")
finally:
    conn.close()
    server.close()