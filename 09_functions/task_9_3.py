# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

def get_int_vlan_map(config_filename): 
    tuple = () 
    final1 = {}
    final2 = {} 
    pred_line=''#предыдущая строчка
    with open(config_filename) as f:
        for line in f:
            if 'interface' in line:
                interface = line.split()[1]
            elif 'trunk allowed vlan' in line:
                trunk = line.split()[-1]
                final2[interface] = []
                final2[interface].append(trunk)#начинаем создавать словарь c trunk vlan когда у нас есть два значения, интерфейс и влан 
            elif 'access vlan' in line:
                access = line.split()[-1]
                final1[interface] = access#начинаем создавать словарь c access vlan когда у нас есть два значения, интерфейс и влан   
            elif 'mode access' in pred_line and 'duplex' in line:
            #проверяет есть ли 'mode access и 'duplex' в двух строчках следующих друг за другом 
                final1[interface] = '1'
            pred_line=line#предыдущая строчка следующая перед строчкой с 'duplex'
    return(tuple + (final1,final2,))
final = get_int_vlan_map('config_sw2.txt')
print(final)
'''
({'FastEthernet0/0': '10', 'FastEthernet0/2': '20', 'FastEthernet1/0': '20', 'FastEthernet1/1': '30', 'FastEthernet1/3': '1', 'FastEthernet2/0': '1', 'FastEthernet2/1': '1'}, {'FastEthernet0/1': ['100,200'], 'FastEthernet0/3': ['100,300,400,500,600'], 'FastEthernet1/2': ['400,500,600']})
'''