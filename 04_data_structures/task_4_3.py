# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

configs = (config.split())[-1].split(',')
print(configs)
