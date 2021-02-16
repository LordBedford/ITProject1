import threading
import time
import random
import socket
import sys
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', int(sys.argv[1]))
print(sys.argv[1])
ss.bind(server_binding)
ss.listen(1)

csockid, addr = ss.accept()
print("[S]: Got a connection request from a client at {}".format(addr))

data = csockid.recv(1000)
data = data.decode("UTF-8","strict")
serverList = {
  "qtsdatacenter.aws.com": "128.64.3.2 A",
  "mx.rutgers.edu": "192.64.4.2 A",
  "kill.cs.rutgers.edu": "182.48.3.2 A",
  "mx.rutgers.edu": "192.64.4.2 A",
  "www.ibm.com": "192.64.4.2 A",
  "www.google.com": "8.6.4.2 A"
}
print("[S]: The requested domain is: ", data)
if data in serverList:
    csockid.send(serverList[data].encode('utf-8'))
else:
    csockid.send("localhost - NS".encode('utf-8'))


# Close the server socket
ss.close()
exit()