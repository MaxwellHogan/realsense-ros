import socket
import time

# def create_udp():
#     sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#     server_address = ('0.0.0.0', 10010)
#     print("starting")
#     sock.bind(server_address)
#     return sock

# def send_stream(sock, client_address):
#     count = 0
#     try:
#         while True:
#             message = f"data {count}".encode()
#             print(message)
#             sent =  sock.sendto(message, client_address)
#             count +=1
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("server stopped")

# if __name__ == "__main__":
#     sock = create_udp()
#     client_address = ('localhost', 10011)
#     send_stream(sock, client_address)

def send_data(ip, port, message):
     sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     server_address = (ip, port)
     sock.connect(server_address)

     try:
        message=message.encode()
        print(message)