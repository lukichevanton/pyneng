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

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

In [69]: ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEtherne
    ...: t0/0'
    
In [70]: ospf_route = ospf_route.replace('O','OSPF')

In [71]: RESULT = ospf_route.split(' ')

In [72]: print('{:20} {:8}'.format('Protocol: ', RESULT[0]))
    ...: print('{:20} {:8}'.format('Prefix: ', RESULT[1]))
    ...: print('{:20} {:8}'.format('AD/Metric: ', RESULT[2]))
    ...: print('{:20} {:8}'.format('Next-Hop: ', RESULT[4]))
    ...: print('{:20} {:8}'.format('Last update: ', RESULT[5]))
    ...: print('{:20} {:8}'.format('Outbound Interface: ', RESULT[6]))
    ...: 
Protocol:            OSPF    
Prefix:              10.0.24.0/24
AD/Metric:           [110/41]
Next-Hop:            10.0.13.3,
Last update:         3d18h,  
Outbound Interface:  FastEthernet0/0