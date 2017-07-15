import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'Pythonprogramming.net'

def port_scan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(0, 26):
    if port_scan(x):
        print'port', x, 'is open!!!!!'
    else:
        print'port', x, 'is closed.'

