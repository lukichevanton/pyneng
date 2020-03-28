# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''

#!/usr/bin/env python3
'''
import subprocess

from tabulate import tabulate

address = ['8.8.8.8', '1.2.3.4', '1.1.1.1', '1.2.3.5']

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

	#tuple_result = tuple(result)
	return(result)

ping = ping_ip_addresses(address)
print(ping)'''

from tabulate import tabulate

test = [{'Reachable': '8.8.8.8',
		'Unreachable': '1.2.3.4'},
		{'Reachable': '1.1.1.1',
		'Unreachable': '1.2.3.5'}]
print(tabulate(test, headers='keys'))