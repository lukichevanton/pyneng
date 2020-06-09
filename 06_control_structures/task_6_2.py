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

'''1ый вариант'''

format = input('Введите IP-адреса в формате 10.0.1.1: ')
ip1,ip2,ip3,ip4 = format.split('.')
if int(ip1) <= 223 and int(ip1) >= 1 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
    print ("unicast")
elif int(ip1) >= 224 and int(ip1) <= 239 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
    print("multicast")
elif format == "255.255.255.255":
    print("local broadcast")
elif format == "0.0.0.0":
    print("unassigned")
else:
    print('unused')

'''2-ой вариант'''

try:
    format = input('Введите IP-адреса в формате 10.0.1.1: ')
    ip1,ip2,ip3,ip4 = format.split('.')
    if int(ip1) <= 223 and int(ip1) >= 1 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
        print ("unicast")
    elif int(ip1) >= 224 and int(ip1) <= 239 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
        print("multicast")
    elif format == "255.255.255.255":
        print("local broadcast")
    elif format == "0.0.0.0":
        print("unassigned")
    else:
        print('unused')
except (ValueError, TypeError, NameError):
    print("unused")

'''
Введите IP-адреса в формате 10.0.1.1: 1.1.1.1
unicast
'''

