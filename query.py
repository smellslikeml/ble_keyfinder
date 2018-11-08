#!/usr/bin/env python
'''
Logs RSSI readings for a targeted BD_ADDR
Labels readings with device location
[Usage]
   python query.py <location_name>
'''
import sys
import time
import configparser
from pssh.clients import ParallelSSHClient

config = configparser.ConfigParser()
config.read('config.ini')
BD_ADDR = config['DEFAULT']['BD_ADDR'] 
INTERVAL = int(config['DEFAULT']['INTERVAL'])
host_lst = config['DEFAULT']['HOSTS']

location = sys.argv[1]

with open(host_lst, 'r') as infile:
    data = infile.readlines()
data = data[1:]   # skip header: ip,user,password
host_lst = [host.strip().split(',') for host in data]
host_config = {}
for host in host_lst:
    try:
        host_config[host[0]] = {'user': host[1], 'password': host[2]}
    except:
        pass
hosts = host_config.keys()
client = ParallelSSHClient(hosts, host_config=host_config)

CMD = './bt_rssi.py {}'.format(BD_ADDR)
with open('bt_logs.txt', 'a') as outfile:
    while True:
        output = client.run_command(CMD, sudo=True)

        dd = {host:'0' for host in list(hosts)}
        for host, host_output in output.items():
            for line in host_output.stdout:
                dd[host] = line
        dd['location'] = location
        outfile.write(str(dd) + '\n')
        print(dd)
        time.sleep(INTERVAL)
