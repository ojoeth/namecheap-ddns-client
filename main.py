#!/usr/bin/env python3
from requests import get
from time import sleep
from sys import argv

def get_ip():
    return get('https://ip.me').text

def update_ddns(host, domain, password, ip):
    get(('https://dynamicdns.park-your-domain.com/update?host='+host+'&domain='+domain+'&password='+password+'&ip='+ip))
    return True

if __name__ == "__main__":
    try:
        host = argv[1]
        domain = argv[2]
        password = argv[3]
    except:
        print("Syntax: main.py <host> <domain> <DDNS Password>")
        exit()

    ip = get_ip()
    print("Updating DDNS...")
    update_ddns(host, domain, password, ip)
    print("done")

    while True:
        ip = get_ip()
        sleep(20)
        ip2 = get_ip()
        if ip != ip2:
            print("IP has been changed... updating DDNS")
            update_ddns(host, domain, password, ip2) 

    
