# -*- coding: utf-8 -*-
"""
Задание 21.2

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding и записать его в файл templates/sh_ip_dhcp_snooping.template

Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* mac - такого вида 00:04:A3:3E:5B:69
* ip - такого вида 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Проверить работу шаблона с помощью функции parse_command_output из задания 21.1.
"""
from netmiko import ConnectHandler
import textfsm
from tabulate import tabulate
from pprint import pprint
from task_21_1 import *#импорт функции из задания task_21_1

output = '''
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
00:04:A3:3E:5B:69   10.1.5.2         63951       dhcp-snooping   5     FastEthernet0/10
00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9
00:09:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/3
Total number of bindings: 4
'''
#функции нет, так как она импортирована из задания task_21_1
result = parse_command_output("templates/sh_ip_dhcp_snooping.template", output)
pprint(result)