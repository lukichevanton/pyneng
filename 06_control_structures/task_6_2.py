# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

"""1-ый вариант"""
ip = input('введите IP-сети в формате 10.0.1.1: ')
ip1,ip2,ip3,ip4 = (ip.split('.'))
ip1 = int(ip1)
ip2 = int(ip2)
ip3 = int(ip3)
ip4 = int(ip4)

if ip1 <= 223 and ip1 >= 1:
    print ("unicast")
elif ip1 >= 224 and ip1 <= 239:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")

"""2-ой вариант"""
try:
   ip = input('Введите IP-сети в формате 1.0.0.255: ')
   ip1,ip2,ip3,ip4 = (ip.split('.'))
except (ValueError, TypeError):
    print("unused")
else:  
    ip1 = int(ip1)
    ip2 = int(ip2)
    ip3 = int(ip3)
    ip4 = int(ip4)
    if ip1 <= 223 and ip1 >= 1 :
        print ("unicast")
    elif ip1 >= 224 and ip1 <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")