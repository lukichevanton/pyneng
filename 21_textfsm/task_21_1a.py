# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
"""
from netmiko import ConnectHandler
import textfsm
from tabulate import tabulate
from pprint import pprint

def parse_command_output(template, command_output):
	final = []
	with open(template) as template:
		fsm = textfsm.TextFSM(template)
		result = fsm.ParseText(command_output)
		intf, address, status, protocol = fsm.header
		for line in result:
			final2 = {}
			intf1, address1, status1, protocol1 = line
			final2[intf] = intf1
			final2[address] = address1
			final2[status] = status1
			final2[protocol] = protocol1
			final.append(final2)
	return final

# вызов функции должен выглядеть так
if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "secret": "C1sco12345",
        "port": "8181",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    pprint(result)
'''
      $ python task_21_1a.py 
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
 {'address': '160.1.1.255',
  'intf': 'Loopback1',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'intf': 'Loopback2',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'intf': 'Loopback2244',
  'protocol': 'up',
  'status': 'up'},
 {'address': '5.5.5.5',
  'intf': 'Loopback5555',
  'protocol': 'up',
  'status': 'up'},
 {'address': '6.6.6.6',
  'intf': 'Loopback6666',
  'protocol': 'up',
  'status': 'up'},
 {'address': '192.168.1.1',
  'intf': 'VirtualPortGroup0',
  'protocol': 'up',
  'status': 'up'}]
 '''