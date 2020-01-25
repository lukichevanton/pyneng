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

Задание 5.1
device = input('Введите имя устройства: ')
print(london_co[device])
print(london_co)

Задание 5.1a
dev = input('Введите имя устройства: ')
param = input('Введите имя параметра: ')
print(london_co[dev][param])

Задание 5.1b
dev = input('Введите имя устройства: ')
param = input('Введите имя параметра ({}): '.format(','.join(list(london_co[dev].keys()))))
print(london_co[dev][param])

Задание 5.1c
dev = input('Введите имя устройства: ')
param = input('Введите имя параметра ({}): '.format(','.join(list(london_co[dev].keys()))))
print(london_co[dev].get(param,'Такого параметра нет'))

Задание 5.1d
dev = input('Введите имя устройства: ')
param = input('Введите имя параметра ({}): '.format(','.join(list(london_co[dev].keys()))))
print(london_co[dev].get(param.upper().lower(),'Такого параметра нет'))
