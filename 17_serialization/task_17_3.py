# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

#!/usr/bin/env python3

from pprint import pprint
import re

def parse_sh_cdp_neighbors(data_filenames):

    f = open('sh_cdp_n_sw1.txt')
    f = f.read()#читаем файл в одну строку и передаем функции parse_sh_version

    def parse_sh_cdp_neighbors(line):
        final2 = {}#{'Eth 0/1': {'R1': 'Eth 0/0'}, 'Eth 0/2': {'R2': 'Eth 0/0'}, 'Eth 0/3': {'R3': 'Eth 0/0'}, 'Eth 0/4': {'R4': 'Eth 0/0'}}
        final3 = {}
        loc_dev = line.split('>')[0].strip('\n')#'\nSW1', .strip('\n') убирает \n пробел, в итоге получается 'SW1'     
        result = re.finditer(r'(?P<rem_dev>\w+\d+) +?'
                            r'(?P<loc_intf>\w+ \S+) +\d+.+? \d+ +'
                            r'(?P<rem_intf>\w+ \S+)', line)#('R1', 'Eth 0/1', 'Eth 0/0')
        for match in result:
            final = {}#{'R1': 'Eth 0/0'}
            rem_dev = match.group('rem_dev')
            loc_intf = match.group('loc_intf')
            rem_intf = match.group('rem_intf')
            final[rem_dev] = rem_intf
            final2[loc_intf] = final
            final3[loc_dev] = final2
        return(final3)
    result_parse = parse_sh_cdp_neighbors(f)
    return(result_parse)

result_csv = parse_sh_cdp_neighbors('sh_cdp_n_sw1.txt')
pprint(result_csv)
'''
{'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}}}
'''