# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

'''1ый вариант'''
while True:
    try:
        format = input('Введите IP-адреса в формате 10.0.1.1: ')
        ip1,ip2,ip3,ip4 = format.split('.') 
        if int(ip1) >= 1 and int(ip1) <= 223 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
            print('unicast')
            break
        elif int(ip1) >= 224 and int(ip1) <= 239 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
            print('multicast')
            break
        elif format == "255.255.255.255":
            print("local broadcast")
            break
        elif format == "0.0.0.0":
            print("unassigned")
        elif int(ip1) >= 256 or int(ip2) >= 256 or int(ip3) >= 256 or int(ip4) >= 256:
            print("Incorrect IPv4 address")
        else:
            print('unused')
    except (ValueError, TypeError, NameError):
        print("Неправильный IP-адрес")
            
'''2ой вариант'''         
while True:
    format = input('Введите IP-адреса в формате 10.0.1.1: ')
    try:
        ip = [int(a) for a in format.split('.')]
        check_range = [byte for byte in ip if 0 <= byte <= 255]
        if not len(check_range) == 4:
            print('Incorrect IPv4 address')
            continue
        elif ip[0] >= 1 and ip[0] <= 223:
            print('unicast')
            break
        elif ip[0] >= 223 and ip[0] <= 239:
            print('multicast')
            break
        elif ip_address == '255.255.255.255':
            print(('ip {} local broadcast').format(ip_address))
            break
        elif ip_address == '0.0.0.0':
            print(('ip {} unassigned').format(ip_address))
            break
        else:
            print('unused')
            break
    except (ValueError, TypeError, NameError):
        print('Incorrect IPv4 address')
        continue
        
'''
Введите IP-адреса в формате 10.0.1.1: 1111
Incorrect IPv4 address
Введите IP-адреса в формате 10.0.1.1: 1.1.1.1
unicast
'''