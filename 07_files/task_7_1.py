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

with open('ospf.txt', 'r') as f:
    for line in f:
        line = line.replace('O','OSPF').replace(',','').replace('[','').replace(']','').split()
        print("{:20} {:10}".format('Protocol:', line[0]))
        print("{:20} {:15}".format('Prefix:', line[1]))
        print("{:20} {:15}".format('AD/Metric:', line[2]))
        print("{:20} {:15}".format('Next-Hop:', line[4]))
        print("{:20} {:15}".format('Last update:', line[5]))
        print("{:20} {:15}".format('Outbound Interface:', line[6]))
'''
Protocol:            OSPF      
Prefix:              10.0.24.0/24   
AD/Metric:           110/41         
Next-Hop:            10.0.13.3      
Last update:         3d18h          
Outbound Interface:  FastEthernet0/0
Protocol:            OSPF      
Prefix:              10.0.28.0/24   
AD/Metric:           110/31         
Next-Hop:            10.0.13.3      
Last update:         3d20h          
Outbound Interface:  FastEthernet0/0
Protocol:            OSPF      
Prefix:              10.0.37.0/24   
AD/Metric:           110/11         
Next-Hop:            10.0.13.3      
Last update:         3d20h          
'''
