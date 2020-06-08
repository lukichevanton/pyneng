# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

mac = 'AAAA:BBBB:CCCC'

mac2 = bin(int((mac.replace(':','')), 16))
print(mac2)
mac = mac.split(':')
mac1 = bin(int(mac[0], 16))+bin(int(mac[1], 16))+bin(int(mac[2], 16))
print(mac1)