# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству и выполняет перечень команд в конфигурационном режиме на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает строку с результатами выполнения команды:

In [7]: r1
Out[7]:
{'device_type': 'cisco_ios',
 'ip': '192.168.100.1',
 'username': 'cisco',
 'password': 'cisco',
 'secret': 'cisco'}

In [8]: commands
Out[8]: ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

In [9]: result = send_config_commands(r1, commands)

In [10]: result
Out[10]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#logging 10.255.255.1\nR1(config)#logging buffered 20010\nR1(config)#no logging console\nR1(config)#end\nR1#'

In [11]: print(result)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.255.255.1
R1(config)#logging buffered 20010
R1(config)#no logging console
R1(config)#end
R1#


Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_config_commands.
"""
#!/usr/bin/env python3

import yaml
import socket
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]

def send_config_commands(device, config_commands):
	result = []
	try:
		with ConnectHandler(**device) as ssh:
			ssh.enable()
			output = ssh.send_config_set(config_commands)
			result.append(output)
	except (NetMikoAuthenticationException, NetMikoTimeoutException, socket.timeout) as error:
		print(error)
	return result
		
if __name__ == "__main__":
	with open("devices2.yaml") as f:
		devices = yaml.safe_load(f)
	for device in devices:
		result = send_config_commands(device, commands)
		for line in result:
			print(line)
'''
18:13 $ python task_19_2.py
config term
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v-1(config)#logging 10.255.255.1
csr1000v-1(config)#logging buffered 20010
csr1000v-1(config)#no logging console
csr1000v-1(config)#end
csr1000v-1#
Connection to device timed-out: cisco_ios 192.168.100.2:22
Connection to device timed-out: cisco_ios 192.168.100.3:22
'''