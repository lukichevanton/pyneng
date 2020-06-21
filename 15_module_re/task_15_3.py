# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

#!/usr/bin/env python3

from pprint import pprint
import re
template = ['object network LOCAL_{}',
        	' host {}',
        	' nat (inside,outside) static interface service tcp {} {}']
def convert_ios_nat_to_asa(filename, filename2):
    final = []
    template = ['object network LOCAL_{}',
        	' host {}',
        	' nat (inside,outside) static interface service tcp {} {}']
    regex = re.compile(r'(?P<ip>[\d\.]+\d) '
                    r'(?P<port1>\d+) \w+ \S+ '
                    r'(?P<port2>\d+)')
    with open(filename) as src, open(filename2, 'w') as dest:
        for line in src:
            result = regex.search(line)
            if result:
                ip = result.group('ip')
                port1 = result.group('port1')
                port2 = result.group('port2')
                final.append('\n'.join(template).format(ip, ip, port1, port2))
                dest.write('\n'.join(template).format(ip, ip, port1, port2))

    return(final)
final = convert_ios_nat_to_asa('cisco_nat_config.txt', 'asa_nat_config.txt')
pprint(final)
'''
['object network LOCAL_10.66.0.13\n'
 ' host 10.66.0.13\n'
 ' nat (inside,outside) static interface service tcp 995 995',
 'object network LOCAL_10.66.0.21\n'
 ' host 10.66.0.21\n'
 ' nat (inside,outside) static interface service tcp 20065 20065',
 'object network LOCAL_10.66.0.22\n'
 ' host 10.66.0.22\n'
 ' nat (inside,outside) static interface service tcp 443 44443',
 ...
 '''