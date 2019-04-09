import socket
import subprocess
import sys
import datetime
from local_machine_info import print_machine_info
import time
import os



print_machine_info()
danas = datetime.date.today()
print danas

		
subprocess.call('', shell=True)
remoteServer    = raw_input("Unesi host za scan ")

try:
	remoteServerIP = socket.gethostbyname(remoteServer)
	print  "Postojeca ip adresa"
except socket.error:
	print "Nepostojeca ip adresa"



port = 80
retry = 1
delay = 1

def isOpen(remoteServerIP, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                s.connect((remoteServerIP, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
			return False
        finally:
                s.close()

def checkHost(remoteServerIP, port):
        ipup = False
        for i in range(retry):
                if isOpen(remoteServerIP, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup

if checkHost(remoteServerIP, port):
        print remoteServerIP + " je aktivan"
		

hostname = remoteServerIP
response = os.system("ping -c 1 " + hostname)
# and then check the response...
if response == 0:
	pingstatus = "Network Active"
else:
	pingstatus = "Network Error"
print hostname
print  pingstatus		

def ping(host):
    """
    vraca true ako host odgovori
    """
    import subprocess, platform


    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    
    return subprocess.call(args, shell=need_sh) == 0



print(ping(remoteServerIP))

start = raw_input("Unesi pocetni port: ") 
end = raw_input("Unesi krajnji port: ")

for port in range(int(start), int(end)):  
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "Skeniram port %d" % port
	result = sock.connect_ex((remoteServerIP, port))
	if result == 0:
		print "Port { %d}: Open" % port
	else:
		print "Port is not open"	
	sock.close()

	






	
