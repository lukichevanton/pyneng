# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

#!/usr/bin/env python3

"""1ый вариант"""
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

template = {
             'access': 'Введите номер VLAN:',
             'trunk': 'Введите разрешенные VLANы:'
             }

template2 = {'access': access_template, 
             'trunk': trunk_template
             }

mode = input('Введите режим работы интерфейса (access/trunk): ')
inter = input('Введите тип и номер интерфейса (Fa0/1): ')        
vlan = input('{}'. format(template[mode]))

print('interface {}'.format(inter))
print('\n'.join(template2[mode]).format(vlan))
'''
Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса (Fa0/1): Fa0/1
Введите номер VLAN:10
interface Fa0/1
switchport mode access
switchport access vlan 10
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
'''

"""2ой вариант"""
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

template = {'access': access_template, 
             'trunk': trunk_template,
             'vlanaccess': 'Введите номер VLAN: ',
             'vlantrunk': 'Введите разрешенные VLANы: '
             }

mode = input('Введите режим работы интерфейса (access/trunk): ')
inter = input('Введите тип и номер интерфейса (Fa0/1): ')

mode_vlan = 'vlan' + mode

vlan = input('{}'. format(template[mode_vlan]))

print('interface {}'.format(inter))
print('\n'.join(template[mode]).format(vlan))
'''
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса (Fa0/1): Fa0/1
Введите разрешенные VLANы: 10,20,30
interface Fa0/1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 10,20,30
'''