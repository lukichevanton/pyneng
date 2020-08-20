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
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetmikoAuthenticationException

command = "sh ip int br"

def send_show_command(device, commands):
	result = []
	try:
		with ConnectHandler(**device) as ssh:
			ssh.enable()
			output = ssh.send_command(command)
			result.append(output)
	except (NetMikoTimeoutException, NetmikoAuthenticationException) as error:
		print(error)
	return result
		
if __name__ == "__main__":
	with open("devices2.yaml") as f:
		devices = yaml.safe_load(f)
	for device in devices:
		result = send_show_command(device, command)
		for line in result:
			print(line)