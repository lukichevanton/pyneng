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
from check_ip_function import check_ip
from tabulate import tabulate

addresses = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

def convert_ranges_to_ip_list(ip_addresses):   
    correct = []#['8.8.4.4']
    notcorrect = []#['1.1.1.1-3','172.21.41.128-172.21.41.132']
    for ip in ip_addresses:
        if check_ip(ip):
            correct.append(ip)
        else:
            notcorrect.append(ip)
    for ip in notcorrect:       
        ip  = ip.split('-')#['1.1.1.1', '3'] или ['172.21.41.128', '172.21.41.132']
        if check_ip(ip[1]):#если ip-адрес типа 172.21.41.132 то:
            ip1 = ip[0].split('.')#['172', '21', '41', '128']
            ip2 = ip[1].split('.')#['172', '21', '41', '132']
            ip3 = ip1[0:3]#['172', '21', '41']
            ip4 = ip2[0:3]#['172', '21', '41']
            ip5 = '.'.join(ip3)+'.'#172.21.41.
            ip6 = '.'.join(ip4)+'.'#172.21.41.
            ip7 = int(ip1[3])#128
            ip8 = int(ip2[3])#132
            list1 = [ip5 + str(i) for i in range(int(ip7),int(ip8)+1)]#['172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']                    
        else:#если ip-адрес не типа 172.21.41.132 то:
            ip1 = ip[0].split('.')#['1', '1', '1', '1']
            ip2 = ip1[0:3]#['1', '1', '1']
            ip3 = '.'.join(ip2)+'.'#1.1.1.
            ip4 = int(ip1[3])#1
            list2 = [ip3 + str(i) for i in range(int(ip4),int(ip[1])+1)]#['1.1.1.1', '1.1.1.2', '1.1.1.3']
    result = correct + list2 + list1
    return result
final_round1 = convert_ranges_to_ip_list(addresses)#['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

def ping_ip_addresses(ip_addresses):
	result = []#[['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3'], ['172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']]
	alive = []#['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3']
	unreachable = []#['172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
	for ip in ip_addresses:
		reply = subprocess.run(['ping', '-c', '1', '-n', ip], stdout=subprocess.DEVNULL)
		if reply.returncode == 0:                         
			alive.append(ip)         
		else:
			unreachable.append(ip)       	
	result.append(alive)
	result.append(unreachable)
	return(result)
final_round2 = ping_ip_addresses(final_round1)#[['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3'], ['172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']]

def print_ip_table(ip_addresses0, ip_addresses1):
	result = tabulate({"Reachable": ip_addresses0, "Unreachable": ip_addresses1}, headers="keys")
	return result
really_final = print_ip_table(final_round2 [0], final_round2 [1])#Создает словарь - {"Reachable": ['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3'], "Unreachable": ['172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']}
print(really_final)

'''
      $ python task_12_3.py 
Reachable    Unreachable
-----------  -------------
8.8.4.4      172.21.41.128
1.1.1.1      172.21.41.129
1.1.1.2      172.21.41.130
1.1.1.3      172.21.41.131
             172.21.41.132
'''