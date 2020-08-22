# -*- coding: utf-8 -*-
"""
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр log,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
"""
#!/usr/bin/env python3

import yaml
import socket
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]

def send_config_commands(device, config_commands, log=True):
	result = []
	try:
		if log:
			print('Подключаюсь к {}...'.format(device['host']))
		with ConnectHandler(**device) as ssh:
			ssh.enable()
			output = ssh.send_config_set(config_commands)
			result.append(output)
	except (NetMikoAuthenticationException, NetMikoTimeoutException, socket.timeout) as error:
		if log:
			print(error)
	return result
		
if __name__ == "__main__":
	with open("devices2.yaml") as f:
		devices = yaml.safe_load(f)
	for device in devices:
		result = send_config_commands(device, commands)
		#for line in result:
		#	print(line)
'''
18:38 $ python task_19_2a.py
Подключаюсь к ios-xe-mgmt-latest.cisco.com...
Подключаюсь к 192.168.100.2...
Connection to device timed-out: cisco_ios 192.168.100.2:22
Подключаюсь к 192.168.100.3...
Connection to device timed-out: cisco_ios 192.168.100.3:22
'''