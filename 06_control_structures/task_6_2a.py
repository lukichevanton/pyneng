# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

'''1ый вариант'''

try:
    format = input('Введите IP-адреса в формате 10.0.1.1: ')
    ip1,ip2,ip3,ip4 = format.split('.')
    if int(ip1) >= 1 and int(ip1) <= 223 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
        print('unicast')
    elif int(ip1) >= 224 and int(ip1) <= 239 and int(ip2) <= 255 and int(ip3) <= 255 and int(ip4) <= 255:
        print('multicast')
    elif format == "255.255.255.255":
        print("local broadcast")
    elif format == "0.0.0.0":
        print("unassigned")
    elif int(ip1) >= 256 or int(ip2) >= 256 or int(ip3) >= 256 or int(ip4) >= 256:
        print("Incorrect IPv4 address")
    else:
       print('unused')
except (ValueError, TypeError, NameError):
    print("Неправильный IP-адрес")

'''2ой вариант'''

try:
    format = input('Введите IP-адреса в формате 10.0.1.1: ')
    ip = [int(a) for a in format.split('.')]
    check_range = [byte for byte in ip if 0 <= byte <= 255]
    if not len(check_range) == 4:
        print('Incorrect IPv4 address')
    elif ip[0] >= 1 and ip[0] <= 223:
            print('unicast')
    elif ip[0] >= 223 and ip[0] <= 239:
            print('multicast')
    elif ip_address == '255.255.255.255':
        print("local broadcast")
    elif ip_address == '0.0.0.0':
        print("unassigned")
    else:
        print('unused')
except (ValueError, TypeError, NameError):
    print("Неправильный IP-адрес")
    
'''
Введите IP-адреса в формате 10.0.1.1: 1.1.1.1
unicast
'''

