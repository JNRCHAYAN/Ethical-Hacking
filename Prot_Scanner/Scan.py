import socket
from IPy import IP


ipadress = input("[+] Enter Target IP to Scan : ")
port = 80
try:
    sock = socket.socket()
    sock.connect((ipadress,port))
    print(f"[+] Port {port} is Open")
    
except:
    print(f"[-] Port {port} is close")


