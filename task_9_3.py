# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:

    словарь портов в режиме access, где ключи номера портов, а значения access VLAN:

{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

    словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

def get_int_vlan_map(config_filename):   
    result = {}
    result2 = {} 
    with open(config_filename) as f:
        for line in f:
            if 'interface' in line:
                interface = line.split()[1]
            elif 'access vlan' in line:
                access = line.split()[-1]
                result[interface] = access
            elif 'trunk allowed vlan' in line:
                trunk = line.split()[-1]
                result2[interface] = trunk
    print(result)
    print(result2)
get_int_vlan_map('config_sw1.txt')

{'FastEthernet0/0': '10', 'FastEthernet0/2': '20', 'FastEthernet1/0': '20', 'FastEthernet1/1': '30'}
{'FastEthernet0/1': '100,200', 'FastEthernet0/3': '100,300,400,500,600','FastEthernet1/2': '400,500,600'}
