# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

#!/usr/bin/env python3

from pprint import pprint
import re

def get_ip_from_cfg(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                intf = re.search(r'\S+$', line).group()
            elif 'ip address' in line:
                ip_mask = re.search(r'(\d+\.\d+\.\d+\.\d+) +(\d+\.\d+\.\d+\.\d+)', line)
                if ip_mask:
                    result[intf] = {}
                    result[intf] = ip_mask.groups()
    return(result)
result = get_ip_from_cfg('config_r1.txt')
pprint(result)
'''
{'Ethernet0/0': ('10.0.13.1', '255.255.255.0'),
 'Ethernet0/2': ('10.0.19.1', '255.255.255.0'),
 'Loopback0': ('10.1.1.1', '255.255.255.255')}
 '''