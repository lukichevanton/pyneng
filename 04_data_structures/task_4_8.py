# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

ip = '192.168.3.1'

print("{:8} {:8} {:8} {:8}".format(ip.split('.')[0],ip.split('.')[1],ip.split('.')[2],ip.split('.')[3]))
print("{:08b} {:08b} {:08b} {:08b}".format(int(ip.split('.')[0]),int(ip.split('.')[1]),int(ip.split('.')[2]),int(ip.split('.')[3])))
'''
192      168      3        1       
11000000 10101000 00000011 00000001
'''