# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

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
			output = ssh.send_command(commands)
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