# -*- coding: utf-8 -*-
"""
Задание 21.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 21.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
"""
from netmiko import ConnectHandler
import textfsm
from tabulate import tabulate
from pprint import pprint
from textfsm import clitable
import yaml
import socket
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

attributes = {
	'Command': 'show ip interface brief',
	'Vendor': 'Cisco',
}

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

def send_and_parse_command_parallel(device, command, templates_path, index='index'):

	start_msg = '===> {} Connection: {}'
	received_msg = '<=== {} Received:   {}'
	ip = device['host']
	logging.info(start_msg.format(datetime.now().time(), ip))

	with ConnectHandler(**device) as ssh:
		ssh.enable()
		output = ssh.send_command(command)
		logging.info(received_msg.format(datetime.now().time(), ip))

	cli_table = clitable.CliTable(index, templates_path)
	cli_table.ParseCmd(output, attributes)
	header = list(cli_table.header)

	data_rows = [list(row) for row in cli_table]
	header = list(cli_table.header)

	final = []
	intf, address, status, protocol = header
	for row in data_rows:
		final2 = {}
		intf1, address1, status1, protocol1 = row
		final2[intf] = intf1
		final2[address] = address1
		final2[status] = status1
		final2[protocol] = protocol1
		final.append(final2)
	return final

with open('devices2.yaml') as f:
	devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
	future_list = []
	for device in devices:
		future = executor.submit(send_and_parse_command_parallel, device, "sh ip int br", "templates", 'index_file')
		future_list.append(future)
	for f in as_completed(future_list):
		pprint(f.result())

'''
      $ python task_21_5.py 
<concurrent.futures.thread.ThreadPoolExecutor object at 0x7f0ec172aac8>_0 root INFO: ===> 21:31:30.832096 Connection: ios-xe-mgmt.cisco.com
<concurrent.futures.thread.ThreadPoolExecutor object at 0x7f0ec172aac8>_0 root INFO: <=== 21:31:40.806866 Received:   ios-xe-mgmt.cisco.com
[{'address': '10.10.20.48',
  'intf': 'GigabitEthernet1',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'intf': 'GigabitEthernet2',
  'protocol': 'down',
  'status': 'administratively down'},
 {'address': 'unassigned',
  'intf': 'GigabitEthernet3',
  'protocol': 'down',
  'status': 'administratively down'},
 {'address': '2.2.2.2', 'intf': 'Loopback1', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned',
  'intf': 'Loopback2',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'intf': 'Loopback3',
  'protocol': 'up',
  'status': 'up'},
 {'address': '4.4.4.4', 'intf': 'Loopback4', 'protocol': 'up', 'status': 'up'},
 {'address': '5.5.5.5', 'intf': 'Loopback99', 'protocol': 'up', 'status': 'up'}]
'''
