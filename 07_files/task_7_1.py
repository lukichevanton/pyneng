# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

"""1-ый вариант через print"""
f = open('ospf.txt')
RESULT = f.read().replace('O','OSPF').replace('[',' ').replace(']',' ').replace(',',' ').replace('        ',' ').replace('  ',' ').split('\n')

a = RESULT[0].split(' ')
b = RESULT[1].split(' ')
c = RESULT[2].split(' ')

print('{:20} {:8}'.format('Protocol: ', a[0]))
print('{:20} {:8}'.format('Prefix: ', a[1]))
print('{:20} {:8}'.format('AD/Metric: ', a[2]))
print('{:20} {:8}'.format('Next-Hop: ', a[4]))
print('{:20} {:8}'.format('Last update: ', a[5]))
print('{:20} {:8}'.format('Outbound Interface: ', a[6]))
print()
print('{:20} {:8}'.format('Protocol: ', b[0]))
print('{:20} {:8}'.format('Prefix: ', b[1]))
print('{:20} {:8}'.format('AD/Metric: ', b[2]))
print('{:20} {:8}'.format('Next-Hop: ', b[4]))
print('{:20} {:8}'.format('Last update: ', b[5]))
print('{:20} {:8}'.format('Outbound Interface: ', b[6]))
print()

"""etc"""

"""2-ой вариант через if"""
f = open('ospf.txt')
RESULT = f.read().replace('O','OSPF').replace('[',' ').replace(']',' ').replace(',',' ').replace('        ',' ').replace('  ',' ').split('\n')

a = RESULT[0].split(' ')
b = RESULT[1].split(' ')
c = RESULT[2].split(' ')

ospf = [
    'Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:'
]
try:
    for command in ospf:
        if command.endswith('Protocol:'):
            print('{:20} {:8}'.format(command, a[0]))
        elif command.endswith('Prefix:'):
            print('{:20} {:8}'.format(command, a[1]))
        elif command.endswith('AD/Metric:'):
            print('{:20} {:8}'.format(command, a[2]))
        elif command.endswith('Next-Hop:'):
            print('{:20} {:8}'.format(command, a[4]))
        elif command.endswith('Last update:'):
            print('{:20} {:8}'.format(command, a[5]))
        elif command.endswith('Outbound Interface:'):
            print('{:20} {:8}'.format(command, a[6]))
except IndexError:
    print('end of list')

print()

try:
    for command in ospf:
        if command.endswith('Protocol:'):
            print('{:20} {:8}'.format(command, b[0]))
        elif command.endswith('Prefix:'):
            print('{:20} {:8}'.format(command, b[1]))
        elif command.endswith('AD/Metric:'):
            print('{:20} {:8}'.format(command, b[2]))
        elif command.endswith('Next-Hop:'):
            print('{:20} {:8}'.format(command, b[4]))
        elif command.endswith('Last update:'):
            print('{:20} {:8}'.format(command, b[5]))
        elif command.endswith('Outbound Interface:'):
            print('{:20} {:8}'.format(command, b[6]))
except IndexError:
    print('end of list')

print()

try:
    for command in ospf:
        if command.endswith('Protocol:'):
            print('{:20} {:8}'.format(command, c[0]))
        elif command.endswith('Prefix:'):
            print('{:20} {:8}'.format(command, c[1]))
        elif command.endswith('AD/Metric:'):
            print('{:20} {:8}'.format(command, c[2]))
        elif command.endswith('Next-Hop:'):
            print('{:20} {:8}'.format(command, c[4]))
        elif command.endswith('Last update:'):
            print('{:20} {:8}'.format(command, c[5]))
        elif command.endswith('Outbound Interface:'):
            print('{:20} {:8}'.format(command, c[6]))
except IndexError:
    print('end of list')
    
"""etc"""
