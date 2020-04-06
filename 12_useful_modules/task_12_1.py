# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

import subprocess

address = ['8.8.8.8','1.2.3.4', '1.1.1.1', '1.2.3.5']

def ping_ip_addresses(ip):
	result = []
	alive = []
	unreachable = []	
	for ip in address:
		reply = subprocess.run(['ping', '-c', '1', '-n', ip])
		if reply.returncode == 0:                         
			alive.append(ip)         
		else:
			unreachable.append(ip)       	
	result.append(alive)
	result.append(unreachable)

	tuple_result = tuple(result)
	return(tuple_result)

ping = ping_ip_addresses(address)
print(ping)
'''
(['8.8.8.8', '1.1.1.1'], ['1.2.3.4', '1.2.3.5'])
'''