# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

In [1]: CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

In [3]: commands = CONFIG.split()

In [7]: vlans = commands[-1].split(',')

In [8]: print(vlans)
['1', '3', '10', '20', '30', '100']
