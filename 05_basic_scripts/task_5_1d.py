# -*- coding: utf-8 -*-
'''
Задание 5.1d

Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.

Пример выполнения скрипта:
$ python task_5_1d.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): IOS
15.4


Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

#!/usr/bin/env python3

london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

'''1-ый вариант'''

dev = input('Введите имя устройства: ')
param = input('Введите имя параметра ({}): '.format(','.join(list(london_co[dev].keys()))))
print(london_co[dev].get(param.upper().lower(),'Такого параметра нет'))
'''
Введите имя устройства: r1
Введите имя параметра (location,vendor,model,ios,ip): IP
10.255.0.1
'''

'''2-ой вариант'''

try:
    dev = input('Введите имя устройства: ') 
    param = input('Введите имя параметра ({}): '.format(','.join(london_co[dev].keys()))).upper().lower()
    print(london_co[dev][param])
except KeyError:
    print('Такого устройства или параметра нет')
    
'''
Введите имя устройства: r1
Введите имя параметра (location,vendor,model,ios,ip): IP
10.255.0.1
'''
