# -*- coding: utf-8 -*-
'''
Задание 5.3

Скрипт должен запрашивать у пользователя:
* информацию о режиме интерфейса (access/trunk)
* номере интерфейса (тип и номер, вида Gi0/3)
* номер VLANа (для режима trunk будет вводиться список VLANов)

В зависимости от выбранного режима, на стандартный поток вывода,
должна возвращаться соответствующая конфигурация access или trunk
(шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса,
а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: Fa0/6
Введите номер влан(ов): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса: Fa0/7
Введите номер влан(ов): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
'''

#!/usr/bin/env python3

"""1ый вариант"""
mode = input('Введите режим работы интерфейса (access/trunk): ')
inter = input('Введите тип и номер интерфейса (Fa0/1): ')

template2 = {
             'access': 'Введите номер VLAN:',
             'trunk': 'Введите разрешенные VLANы:'}
             
vlan = input('{}'. format(template2[mode]))

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
             'trunk': trunk_template
             }

print('interface {}'.format(inter))
print('\n'.join(template[mode]).format(vlan))


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
             'vlanaccess': 'Введите номер VLAN:',
             'vlantrunk': 'Введите разрешенные VLANы:'
             }

mode = input('Введите режим работы интерфейса (access/trunk): ')
inter = input('Введите тип и номер интерфейса (Fa0/1): ')

mode_vlan = 'vlan' + mode

vlan = input('{}'. format(template[mode_vlan]))

print('interface {}'.format(inter))
print('\n'.join(template[mode]).format(vlan))
