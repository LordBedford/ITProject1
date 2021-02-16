import socket

def client():
    #open input folder and store lines in sites list
    with open('PROJI-HNS.txt') as f:
        sites = f.readlines()

    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    #send 2 strings to server
    cs.send("www.google.com".encode('utf-8'))
    data_from_server = cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
    cs.send("MX.RUTGERS.EDU".encode('utf-8'))
    #data_from_server = cs.recv(100)
    #print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # close the client socket
    cs.close()
    exit()

client()
