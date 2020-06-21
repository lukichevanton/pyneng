# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""

#!/usr/bin/env python3

from pprint import pprint

import re

def generate_description_from_cdp(filename):
    template = ['description Connected to {} port {}']
    dic = {}
    final = []
    regex = re.compile(r'(?P<remdev>^\w+) +'
                    r'(?P<locintf>\w+ \S+).+ +'
                    r'(?P<remintf>\w+ \S+)')
    with open(filename) as f:
        for line in f:
            result = regex.search(line)
            if result:
                remdev = result.group('remdev')
                locintf = result.group('locintf')
                remintf = result.group('remintf')
                dic[locintf] = {}
                final = ('\n'.join(template).format(remdev, remintf))
                dic[locintf] = final           
    return(dic)
result = generate_description_from_cdp('sh_cdp_n_sw1.txt')
pprint(result)
'''
{'Eth 0/1': 'description Connected to R1 port Eth 0/0',
 'Eth 0/2': 'description Connected to R2 port Eth 0/0',
 'Eth 0/3': 'description Connected to R3 port Eth 0/0',
 'Eth 0/5': 'description Connected to R6 port Eth 0/1'}
'''