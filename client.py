import socket
import sys

def client(request,port):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    ts_port = int(sys.argv[2])

    # Define the port on which you want to connect to the server
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    #encode request and send it to root server
    cs.send(request.encode('utf-8'))

    #recieve data from server
    data_from_server = cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    #if the rs server respons with "localhost - NS" call client again on the
    if data_from_server.decode('utf-8') == "localhost - NS":
        data_from_server = client( request, ts_port)


    # close the client socket
    cs.close()
    return data_from_server

def client_driver():

    rs_port = int(sys.argv[1])
    print(rs_port)

    # open input folder and store lines in sites list
    with open('PROJI-HNS.txt') as f:
        sites = f.readlines()

    #List of thruples to store responses
    responses = list()

    #create connection and send request to RS for each website
    for site in sites:
        site = site.rstrip('\n')
        print(site)
        response = client(site,rs_port)
        responses.append( (site, response) )

    print( responses )


client_driver()