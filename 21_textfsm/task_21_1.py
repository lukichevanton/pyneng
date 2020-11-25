# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM (templates/sh_ip_int_br.template)
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды sh ip int br с оборудования и шаблоне templates/sh_ip_int_br.template.

"""
from netmiko import ConnectHandler
import textfsm
from tabulate import tabulate
from pprint import pprint

def parse_command_output(template, command_output):
	with open(template) as template:
		fsm = textfsm.TextFSM(template)
		result = fsm.ParseText(command_output)

	pprint(fsm.header)
	pprint(result)
	print(tabulate(result, headers = fsm.header))

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
    print(result)
'''
      $ python task_21_1.py 
['intf', 'address', 'status', 'protocol']
[['GigabitEthernet1', '10.10.20.48', 'up', 'up'],
 ['GigabitEthernet2', 'unassigned', 'administratively down', 'down'],
 ['GigabitEthernet3', 'unassigned', 'administratively down', 'down'],
 ['Loopback1', '1.1.1.1', 'up', 'up'],
 ['Loopback2244', 'unassigned', 'up', 'up'],
 ['Loopback5555', '5.5.5.5', 'up', 'up'],
 ['Loopback6666', '6.6.6.6', 'up', 'up'],
 ['VirtualPortGroup0', '192.168.1.1', 'up', 'up']]
 '''