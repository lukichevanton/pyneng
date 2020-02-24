# -*- coding: utf-8 -*-
'''

Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта выглядит так:

interface FastEthernet0/20
    switchport mode access
    duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

def get_int_vlan_map(config_filename):   
    result = {}
    result2 = {} 
    pred_line=''#предыдущая строчка
    with open(config_filename) as f:
        for line in f:
            if 'interface' in line:
                interface = line.split()[1]
            if 'access vlan' in line:
                access = line.split()[-1]
                result[interface] = access    
            elif 'mode access' in pred_line and 'duplex' in line
            #проверяет есть ли 'mode access и 'duplex' в двух строчках следующих друг за другом 
                result[interface] = '1'
            elif 'trunk allowed vlan' in line:
                trunk = line.split()[-1]
                result2[interface] = trunk
            pred_line=line#предыдущая строчка следующая перед строчкой с 'duplex'
    print(result)
    print(result2)
    return(result)
    return(result2)
get_int_vlan_map('config_sw2.txt')

{'FastEthernet0/0': '10', 'FastEthernet0/2': '20', 'FastEthernet1/0': '20', 'FastEthernet1/1': '30', 'FastEthernet1/3': '1', 'FastEthernet2/0':'1', 'FastEthernet2/1': '1'}{'FastEthernet0/1': '100,200', 'FastEthernet0/3': '100,300,400,500,600', 'FastEthernet1/2': '400,500,600'}
