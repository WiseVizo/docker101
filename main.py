import time
import socket
from sklearn.datasets import load_iris

data = load_iris()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))

server.listen()
print(f"[started server]: at {server}")
while True:
    client, addr = server.accept()
    print(f"conntection from : {addr}")
    client.send("you have connected\n".encode())
    client.send(f"{data['data'][:,0]}\n".encode())
    time.sleep(2)
    client.send("disconnecting...\n".encode())
    client.close()
