import socket
from time import perf_counter


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = "127.0.0.1"
    port = 1734

    sock.bind((host, port))

    print("SERVER STARTED!\n WAITING FOR MESSAGES...")

    data, addr = sock.recvfrom(1024)
    print(f"RECEIVED DATA FROM {addr}")
    print(f"CLIENT >> {data.decode('utf-8')}")

    msg = input("SERVER >> ")
    sock.sendto(msg.encode('utf-8'), addr)

    sock.close()


if __name__ == "__main__":
    start = perf_counter()
    server()
    end = perf_counter()
    execution_time = (end - start)
    print(f"TIME >> {execution_time}")