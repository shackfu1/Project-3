import socket
import time

def system_seconds_since_1900():
    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

s = socket.socket()
port = 37
dest = ("time.nist.gov", port)
s.connect(dest)
http = 'GET / HTTP/1.1\r\nHost: time.nist.gov\r\nConnection: close\r\n\r\n '
s.sendall(http.encode())


data = s.recv(40)
if data != b'':
    data = int.from_bytes(data)
print("NIST time: " + str(data) + "\n", end="")
print("system time: " + str(system_seconds_since_1900()))
s.close()