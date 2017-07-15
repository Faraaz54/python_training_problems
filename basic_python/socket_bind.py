import socket
import thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 5555

try:
    s.bind((host, port))

except socket.error, e:
    print str(e)

s.listen(5)
print('Waiting for a connection.')

def threaded_client(conn):
    conn.send('welcome--type ur info\n')

    while True:
        data = conn.recv(2048)
        reply = '\nserver output:'+data+'Recieved'
        if not data:
            break
        conn.sendall(reply)
    conn.close()

while True:

    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    thread.start_new_thread(threaded_client,(conn,))

#conn, addr = s.accept()

#print('connected to '+addr[0]+':'+str(addr[1]))