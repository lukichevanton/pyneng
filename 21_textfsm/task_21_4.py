# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
"""
from netmiko import ConnectHandler
import textfsm
from tabulate import tabulate
from pprint import pprint
from textfsm import clitable
import yaml
import socket
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

r1_params = {
        "device_type": "cisco_ios",
        "host": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "secret": "C1sco12345",
        "port": "8181",
    }

attributes = {
	'Command': 'show ip interface brief',
	'Vendor': 'Cisco',
}

def parse_command_dynamic(device_dict, command, templates_path, index='index'):
	with ConnectHandler(**device_dict) as r1:
		r1.enable()
		output = r1.send_command(command)

	cli_table = clitable.CliTable(index, templates_path)
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

result = parse_command_dynamic(r1_params, "sh ip int br", "templates", 'index_file')
pprint(result)
'''
      $ python task_21_4.py 
[{'address': '10.10.20.48',
  'intf': 'GigabitEthernet1',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'intf': 'GigabitEthernet2',
  'protocol': 'down',
  'status': 'administratively down'},
 {'address': 'unassigned',
  'intf': 'GigabitEthernet3',
  'protocol': 'down',
  'status': 'administratively down'},
 {'address': '2.2.2.2', 'intf': 'Loopback1', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned',
  'intf': 'Loopback2',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'intf': 'Loopback3',
  'protocol': 'up',
  'status': 'up'},
 {'address': '4.4.4.4', 'intf': 'Loopback4', 'protocol': 'up', 'status': 'up'},
 {'address': '5.5.5.5', 'intf': 'Loopback99', 'protocol': 'up', 'status': 'up'}]
 '''
