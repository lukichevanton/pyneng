# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

#!/usr/bin/env python3

'''1ый вариант'''

from datetime import datetime
import time
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
import logging

import netmiko
import yaml

import subprocess

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

ip_list = ['8.8.8.8', '1.2.3.4', '1.1.1.1', '1.2.3.5']

def ping_ip_addresses(ip):

	start_msg = '===> {} Connection: {}'
	received_msg = '<=== {} Received:   {}'
	logging.info(start_msg.format(datetime.now().time(), ip))
	reply = subprocess.run(['ping', '-c', '1', '-n', ip])
	logging.info(received_msg.format(datetime.now().time(), ip))

	return(reply)

with ThreadPoolExecutor(max_workers=3) as executor:
	result = executor.map(ping_ip_addresses, ip_list)

	final = []
	alive = []
	unreachable = []

	for ip, output in zip(ip_list, result):
		print(ip, output)
		
		if output.returncode == 0:                         
			alive.append(ip)         
		else:
			unreachable.append(ip)
	final.append(alive)
	final.append(unreachable)
	tuple_result = tuple(final)
	print(tuple_result)

'''2ой вариант'''
'''
from datetime import datetime
import time
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
import logging

import netmiko
import yaml

import subprocess

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

def ping_ip_addresses(device):

	start_msg = '===> {} Connection: {}'
	received_msg = '<=== {} Received:   {}'
	ip = device['host']
	logging.info(start_msg.format(datetime.now().time(), ip))
	reply = subprocess.run(['ping', '-c', '1', '-n', ip])
	logging.info(received_msg.format(datetime.now().time(), ip))

	return(reply)

with open('devices.yaml') as f:
	devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
	result = executor.map(ping_ip_addresses, devices)

	final = []
	alive = []
	unreachable = []

	for device, output in zip(devices, result):
		print(device['host'], output)

		if output.returncode == 0:                         
			alive.append(device['host'])         
		else:
			unreachable.append(device['host'])
	final.append(alive)
	final.append(unreachable)
	tuple_result = tuple(final)
	print(tuple_result)
'''
'''
(['8.8.8.8', '1.1.1.1'], ['1.2.3.4', '1.2.3.5'])
'''
