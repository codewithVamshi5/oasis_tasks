import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 56789))
print("Connected to the server. Type 'exit' to leave the chat.")

while True:
    msg = input("You: ")
    client.send(msg.encode())
    if msg.lower() == 'exit':
        break

    reply = client.recv(1024).decode()
    if reply.lower() == 'exit':
        print("Server ended the chat.")
        break
    print("Server:", reply)

client.close()
