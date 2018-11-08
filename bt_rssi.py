#!/usr/bin/env python
import subprocess


def rssi_vals(addr):
    try:
        p = subprocess.Popen('sudo btmgmt find | grep {}'.format(addr), stdout=subprocess.PIPE, shell=True)
        a, b = p.communicate()
        read_lst = []
        for reading in str(a).split('\\n')[:-1]:
            reading = reading.split('rssi ')[1]
            reading = reading.split(' flags')[0]
            reading = int(reading)
            read_lst.append(reading)
        return read_lst
    except:
        return

if __name__ == '__main__':
    import sys
    addr = sys.argv[1]
    rssi_est = rssi_vals(addr)
    if rssi_est:
        print(sum(rssi_est) / len(rssi_est))
