# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

"""

#!/usr/bin/env python3

import glob
sh_cdp_neighbors = glob.glob("sh_cdp*")#ищет все файлы в директории начинающиеся на sh_cdp и передаем их функции generate_topology_from_cdp в виде списка в качестве первого аргумента
#print(sh_cdp_neighbors)#

from pprint import pprint
import re
import yaml

def generate_topology_from_cdp(list_of_files, save_to_filename=False):#топология сохраняется только, если save_to_filename как аргумент указано имя файла
    final3 = {}
    '''
    {'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}},
    'R2': {'Eth 0/0': {'SW1': 'Eth 0/2'},
        'Eth 0/1': {'R5': 'Eth 0/0'},
        'Eth 0/2': {'R6': 'Eth 0/1'}}...
        '''
    for files in list_of_files:
        f = open(files)
        f = f.read()#читаем файл в одну строку и передаем функции parse_sh_version

        def parse_sh_cdp_neighbors(line):
            final2 = {}#{'Eth 0/1': {'R1': 'Eth 0/0'}, 'Eth 0/2': {'R2': 'Eth 0/0'}, 'Eth 0/3': {'R3': 'Eth 0/0'}, 'Eth 0/4': {'R4': 'Eth 0/0'}}
            loc_dev = line.split('>')[0].strip('\n')#'\nSW1', .strip('\n') убирает \n пробел, в итоге получается 'SW1'     
            result = re.finditer(r'(?P<rem_dev>\w+\d+) +?'
                                r'(?P<loc_intf>\w+ \S+).+'
                                r' +(?P<rem_intf>\w+ \S+)', line)#('R1', 'Eth 0/1', 'Eth 0/0')
            for match in result:
                final = {}#{'R1': 'Eth 0/0'}
                rem_dev = match.group('rem_dev')
                loc_intf = match.group('loc_intf')
                rem_intf = match.group('rem_intf')
                final[rem_dev] = rem_intf
                final2[loc_intf] = final
                final3[loc_dev] = final2
            return(final2)
            #print(final2)
        result_parse = parse_sh_cdp_neighbors(f)
    
    if save_to_filename:#если save_to_filename как аргумент указано имя файла, то топология сохраняется в файл
        with open(save_to_filename, 'w') as f:
            yaml.dump(final3, f, default_flow_style=False)
        with open(save_to_filename) as f:
            print(f.read())
 
    return(final3)
result_yaml = generate_topology_from_cdp(sh_cdp_neighbors, 'topology.yaml')#топология сохраняется только, если save_to_filename как аргумент указано имя файла
#pprint(result_yaml)
'''
R1:
  Eth 0/0:
    SW1: Eth 0/1
R2:
  Eth 0/0:
    SW1: Eth 0/2
  Eth 0/1:
    R5: Eth 0/0
  Eth 0/2:
    R6: Eth 0/1...
'''