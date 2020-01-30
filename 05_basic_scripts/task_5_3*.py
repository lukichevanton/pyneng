#!/usr/bin/env python3

Задание 5.3
mode = input('Введите режим работы интерфейса (access/trunk): ')
inter = input('Введите тип и номер интерфейса (Fa0/1): ')
vlan = input('Введите номер влан(ов): ')

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

template = {'access' : access_template, 'trunk' : trunk_template}

print('interface {}'.format(inter))
print('\n'.join(template[mode]).format(vlan))

Задание 5.3a
mode = input('Введите режим работы интерфейса (access/trunk): ')
inter = input('Введите тип и номер интерфейса (Fa0/1): ')

vl  = {'access' : 'Введите номер VLAN: ', 'trunk' : 'Введите разрешенные VLANы: '}
vlan = input(vl[mode])

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
template = {'access' : access_template, 'trunk' : trunk_template}

print('interface {}'.format(inter))
print('\n'.join(template[mode]).format(vlan))
