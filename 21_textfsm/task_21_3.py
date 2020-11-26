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