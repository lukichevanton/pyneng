# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

In [48]: command1 = 'switchport trunk allowed vlan 1,2,3,5,8'

In [49]: command2 = 'switchport trunk allowed vlan 1,3,8,9'

In [50]: vlans1 = command1.split()

In [51]: vlans2 = command2.split()

In [52]: vlans1 = vlans1[4].split(',')

In [53]: vlans2 = vlans2[4].split(',')

In [54]: vlans1 = set(vlans1)

In [55]: vlans2 = set(vlans2)

In [60]: Total = vlans1 & vlans2

In [64]: Total = list(Total)

In [68]: print(Total)
['1', '3', '8']


""""""


In [100]: command1 = 'switchport trunk allowed vlan 1,2,3,5,8'

In [101]: command2 = 'switchport trunk allowed vlan 1,3,8,9'

In [102]: vlans = list(set((command1.split())[-1].split(',')) & set((command2.sp
     ...: lit())[-1].split(',')))

In [103]: print(vlans)
['1', '3', '8']


""""""


command1 = 'switchport trunk allowed vlan 1,2,3,5,8'.split()
command2 = 'switchport trunk allowed vlan 1,3,8,9'.split()
vlans = list(set(command1[-1].split(',')).intersection(set(command2[-1].split(','))))
print(vlans)


