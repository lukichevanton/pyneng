# -*- coding: utf-8 -*-
"""
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""
#!/usr/bin/env python3

import yaml
import socket
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

command = "sh ip int br"

def send_show_command(device, commands):
	result = []
	try:
		with ConnectHandler(**device) as ssh:
			ssh.enable()
			output = ssh.send_command(commands)
			result.append(output)
	except (NetMikoAuthenticationException, NetMikoTimeoutException, socket.timeout) as error:
		print(error)
	return result
		
if __name__ == "__main__":
	with open("devices2.yaml") as f:
		devices = yaml.safe_load(f)
	for device in devices:
		result = send_show_command(device, command)
		for line in result:
			print(line)
'''
18:09 $ python task_19_1.py
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      
GigabitEthernet2       192.169.1.1     YES manual up                    up      
GigabitEthernet3       192.168.6.1     YES other  up                    up      
Connection to device timed-out: cisco_ios 192.168.100.2:22
Connection to device timed-out: cisco_ios 192.168.100.3:22

18:13 $ python task_19_1.py
Authentication failure: unable to connect cisco_ios ios-xe-mgmt-latest.cisco.com:8181
Authentication failed.
Connection to device timed-out: cisco_ios 192.168.100.2:22
Connection to device timed-out: cisco_ios 192.168.100.3:22
'''