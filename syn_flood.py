# This is a sample Python script.
import socket
import time

host = input('Enter the IP address of the target: ')
port = int(input('Enter the port of the target: '))
num_packets = int(input('Enter the number of packets to send: '))

for i in range(0,num_packets):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(b'TCP SYN packet')
    print('Packet ', i+1, 'sent')
    s.close()
    time.sleep(0.5)

print('Done!')