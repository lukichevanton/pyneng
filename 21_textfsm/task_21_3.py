# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""
from netmiko import ConnectHandler
import textfsm
from tabulate import tabulate
from pprint import pprint
from textfsm import clitable

attributes = {
	'Command': 'show ip interface brief',
	'Vendor': 'Cisco',
}

def parse_command_dynamic(command_output, attributes_dict, index_file, templ_path):

	output = open(command_output).read()
	cli_table = clitable.CliTable(index_file, templ_path)
	cli_table.ParseCmd(command_output, attributes_dict)
	cli_table.ParseCmd(output, attributes)
	header = list(cli_table.header)

	data_rows = [list(row) for row in cli_table]
	header = list(cli_table.header)

	final = []
	intf, address, status, protocol = header
	for row in data_rows:
		final2 = {}
		intf1, address1, status1, protocol1 = row
		final2[intf] = intf1
		final2[address] = address1
		final2[status] = status1
		final2[protocol] = protocol1
		final.append(final2)
	return final
	
result = parse_command_dynamic('output/sh_ip_int_br.txt', attributes, 'index_file', 'templates')
pprint(result)
'''
      $ python task_21_3.py 
[{'address': '15.0.15.1',
  'intf': 'FastEthernet0/0',
  'protocol': 'up',
  'status': 'up'},
 {'address': '10.0.12.1',
  'intf': 'FastEthernet0/1',
  'protocol': 'up',
  'status': 'up'},
 {'address': '10.0.13.1',
  'intf': 'FastEthernet0/2',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'intf': 'FastEthernet0/3',
  'protocol': 'up',
  'status': 'up'},
 {'address': '10.1.1.1', 'intf': 'Loopback0', 'protocol': 'up', 'status': 'up'},
 {'address': '100.0.0.1',
  'intf': 'Loopback100',
  'protocol': 'up',
  'status': 'up'}]