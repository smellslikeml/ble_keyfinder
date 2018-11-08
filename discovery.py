#!/home/funk/anaconda3/bin/python
import sys
import configparser
from bluetooth.ble import DiscoveryService

def find_dev(dev_name):
    service = DiscoveryService()
    while True:
        devices = service.discover(2)
        for address, name in devices.items():
            if dev_name in name:
                return address

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        dev_name = config['DEFAULT']['DEV_NAME']
    except:
        dev_name = input('Enter the name of the bluetooth beacon: ')
        with open('config.ini', 'a') as outfile:
            outfile.write('DEV_NAME=' + dev_name + '\n')
    try:
        bd_addr = config['DEFAULT']['BD_ADDR']
    except:
        addr = find_dev(dev_name)
        with open('config.ini', 'a') as outfile:
            outfile.write('BD_ADDR=' + addr + '\n')
    print('Configuration Complete!')
