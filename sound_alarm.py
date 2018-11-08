#!/usr/bin/env python
import pexpect
from time import sleep


def sound_alarm(BD_ADDR):
    child = pexpect.spawn('gatttool -I')
    child.sendline('connect {}'.format(BD_ADDR))
    child.expect('Connection successful', timeout=60)
    child.sendline('char-write-cmd 0x000b 0100111000000001')

if __name__ == "__main__":
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    BD_ADDR = config['DEFAULT']['BD_ADDR'] 
    flag = False
    num_attempts = 0
    while not flag and num_attempts < 5:
        print('Attempting to trigger alarm')
        try:
            sound_alarm(BD_ADDR)
            flag = True
        except:
            sleep(2)
            pass
        num_attempts += 1
    
