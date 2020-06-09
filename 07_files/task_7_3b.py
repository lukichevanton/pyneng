# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

vl = input('Введите номер VLAN: ') 

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if '.' in line:
            vlan,mac,typ,port = line.split()
            if vl == vlan:
                print('{:<5} {:16} {:<5}'.format(vlan,mac,port))
'''
Введите номер VLAN: 10
10    0a1b.1c80.7000   Gi0/4
10    01ab.c5d0.70d0   Gi0/8
'''