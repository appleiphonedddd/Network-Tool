import socket
import subprocess
import sys
import time
import os
import speedtest
import netifaces
from requests import get
from datetime import datetime
from pygeocoder import Geocoder

def Port_scanner():

    subprocess.call("clear", shell=True)
    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("_" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("_" *60)

    t1 = datetime.now()

    try:

        for port in range (1,65535):

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))

            if result ==0:

                print("Port {}:        Open".format(port))
                sock.close()

    except KeyboardInterrupt:

        print("interrupt")
        sys.exit()

    except socket.gaierror:

        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:

        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()
    total = t2 - t1
    print("Scanning Completed in in ", total)

def Internet_speedtest():

    try:

        wifi = speedtest.Speedtest()
        wifi.get_best_server()
        wifi.download()
        wifi.upload()
        res = wifi.results.dict()
        print("Download: ", res["download"])
        print("Upload: ", res["upload"])
        print("Ping: ", res["ping"],"ms")

    except KeyboardInterrupt:

        print("interrupt")
        sys.exit()

def ping():
   
    try:

        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         
        host = input("destination: ")
        port = 53
 
        server_address = (host, port)
         
        s.connect(server_address)
 
    except OSError as error:

        print("disConnect,Please check your estination is true!! ")
        return False

    else:
        
        print("Connecting!")
        s.close()
        return True

def Network_interface():

    try:

        IP = get('https://api.ipify.org').text
        interface = input("Input network interface: ")
        address = netifaces.ifaddresses(interface)
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)
        print(address[netifaces.AF_LINK])
        print("Public IP address:", IP) 
        print("Your Computer Name is:"+hostname)   
        print("Your Computer IP Address is:"+IPAddr)   

    except:

        print("Error Network interface,please check your input infomation is true!!")
        return False

def Ping_Lan():

    for ping in range(1,255):

        address = "192.167.2." + str(ping)
        res = subprocess.call(["ping", "-c", "1", address])

        if res == 0:

            print("ping to", address, "OK")

        elif res == 2:

            print("no response from", address)

        else:

            print("ping to", address, "failed!")

function = int(input("Please choose function: "))

if  function == 1:
    Port_scanner()

if  function == 2:
    Internet_speedtest()

if  function == 3:
    ping()

if  function == 4:
    Network_interface()

if  function == 5:
    Ping_Lan()
