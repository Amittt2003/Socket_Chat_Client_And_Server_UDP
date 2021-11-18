import socket
from time import perf_counter


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = "127.0.0.1"
    port = 1734

    msg = input("CLIENT >> ")
    sock.sendto(msg.encode('utf-8'), (host, port))

    data, remote_addres = sock.recvfrom(1024)
    print(f"SERVER >> {str(data)}")

    sock.close()


if __name__ == "__main__":
    start = perf_counter()
    client()
    end = perf_counter()
    execution_time = (end - start)
    print(f"TIME >> {execution_time}")