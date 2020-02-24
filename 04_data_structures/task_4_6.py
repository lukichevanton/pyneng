# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.replace('O','OSPF').replace(',',' ').split()
print("{:20} {:15}".format('Protocol:', ospf_route[0]))
print("{:20} {:15}".format('Prefix:', ospf_route[1]))
print("{:20} {:15}".format('AD/Metric:', ospf_route[2]))
print("{:20} {:15}".format('Next-Hop:', ospf_route[4]))
print("{:20} {:15}".format('Last update:', ospf_route[5]))
print("{:20} {:15}".format('Outbound Interface:', ospf_route[6]))
