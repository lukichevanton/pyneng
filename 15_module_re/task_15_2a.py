# -*- coding: utf-8 -*-
"""
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up')]

Функция должна вернуть такой список со словарями:
[{'interface': 'FastEthernet0/0', 'address': '10.0.1.1', 'status': 'up', 'protocol': 'up'},
 {'interface': 'FastEthernet0/1', 'address': '10.0.2.1', 'status': 'up', 'protocol': 'up'}]

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функция parse_sh_ip_int_br из задания 15.2, если ей как аргумент передать sh_ip_int_br.txt.

Функцию parse_sh_ip_int_br не нужно копировать.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

#!/usr/bin/env python3

from pprint import pprint
import re

headers = ["interface", "address", "status", "protocol"]

data = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'), ('FastEthernet0/1', '10.0.12.1', 'up', 'up'), ('FastEthernet0/2', '10.0.13.1', 'up', 'up'), ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'), ('Loopback0', '10.1.1.1', 'up', 'up'), ('Loopback100', '100.0.0.1', 'up', 'up')]

def convert_to_dict(filename, filename2):
    result = []
    for line_data in filename2:
        final = {}
        for line_head in range(4):#c помощью 'range' указывается диапазон значений для создания словаря
            final[filename[line_head]] = line_data[line_head]#создается словарь из значений в списке headers и data, при этом берется первое значение из headers, как 'key' и первое значение из первого кортежа в data, как 'value'. Аналогично перебираются все значения.
        result.append(final)
    return(result)
result = convert_to_dict(headers, data)
pprint(result)
'''
[{'address': '15.0.15.1',
  'interface': 'FastEthernet0/0',
  'protocol': 'up',
  'status': 'up'},
 {'address': '10.0.12.1',
  'interface': 'FastEthernet0/1',
  'protocol': 'up',
  'status': 'up'},
 {'address': '10.0.13.1',
  'interface': 'FastEthernet0/2',
  'protocol': 'up',
  'status': 'up'},
 {'address': 'unassigned',
  'interface': 'FastEthernet0/3',
  'protocol': 'down',
  'status': 'administratively down'},
 {'address': '10.1.1.1',
  'interface': 'Loopback0',
  'protocol': 'up',
  'status': 'up'},
 {'address': '100.0.0.1',
  'interface': 'Loopback100',
  'protocol': 'up',
  'status': 'up'}]
  '''