# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

#!/usr/bin/env python3

from pprint import pprint
import re

def get_ints_without_description(filename):
    all_intf = []#['Loopback0', 'Tunnel0', 'Ethernet0/0', 'Ethernet0/1', 'Ethernet0/2', 'Ethernet0/3', 'Ethernet0/3.100', 'Ethernet1/0']
    desc_intf = []#['Ethernet0/0', 'Ethernet0/2', 'Ethernet0/3']
    nodesc_intf = []
    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                match = re.search('interface (?P<intf>\S+)', line)
                if match:
                    all_intf.append(match.group(1))#добавляяем все интерфейсы, без исключения в список all_intf
            elif ' description' in line:
                desc_intf.append(match.group(1))#добавляем интерфейсы с description в список desc_intf
        for line in all_intf:#делаем сравнение двух списков
            if line in desc_intf:
                continue
            else:
                nodesc_intf.append(line)#создаем новый список интерфейсов без description
    return(nodesc_intf)
result = get_ints_without_description('config_r1.txt')
pprint(result)
'''
['Loopback0', 'Tunnel0', 'Ethernet0/1', 'Ethernet0/3.100', 'Ethernet1/0']
'''