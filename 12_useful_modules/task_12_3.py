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

import subprocess

from tabulate import tabulate

addresses = ['8.8.8.8', '1.2.3.4', '1.1.1.1', '1.2.3.5']

def ping_ip_addresses(ip):
	result = []#[['8.8.8.8', '1.1.1.1'], ['1.2.3.4', '1.2.3.5']]
	alive = []#['8.8.8.8', '1.1.1.1']
	unreachable = []#['1.2.3.4', '1.2.3.5']
	for ip in addresses:
		reply = subprocess.run(['ping', '-c', '1', '-n', ip], stdout=subprocess.DEVNULL)
		if reply.returncode == 0:                         
			alive.append(ip)         
		else:
			unreachable.append(ip)       	
	result.append(alive)
	result.append(unreachable)
	return(result)
addresses2 = ping_ip_addresses(addresses)#[['8.8.8.8', '1.1.1.1'], ['1.2.3.4', '1.2.3.5']]

def print_ip_table(ip0, ip1):
	result = tabulate({"Reachable": ip0, "Unreachable": ip1}, headers="keys")
	#Создает словарь - {"Reachable": ['8.8.8.8', '1.1.1.1'], "Unreachable": ['1.2.3.4', '1.2.3.5']}
	return(result)
final = print_ip_table(addresses2 [0], addresses2 [1])
print(final)

'''
#Объединяет две функции в одну
def ping_ip_addresses(ip):
	result = []#[['8.8.8.8', '1.1.1.1'], ['1.2.3.4', '1.2.3.5']]
	alive = []#['8.8.8.8', '1.1.1.1']
	unreachable = []#['1.2.3.4', '1.2.3.5']
	for ip in addresses:
		reply = subprocess.run(['ping', '-c', '1', '-n', ip], stdout=subprocess.DEVNULL)
		if reply.returncode == 0:                         
			alive.append(ip)         
		else:
			unreachable.append(ip)       	
	result.append(alive)
	result.append(unreachable)
	result = tabulate({"Reachable": alive, "Unreachable": unreachable}, headers="keys")
	#Создает словарь - {"Reachable": ['8.8.8.8', '1.1.1.1'], "Unreachable": ['1.2.3.4', '1.2.3.5']}
	return(result)
addresses2 = ping_ip_addresses(addresses)
print(addresses2)
'''
'''
      $ python task_12_3.py 
Reachable    Unreachable
-----------  -------------
8.8.8.8      1.2.3.4
1.1.1.1      1.2.3.5
'''