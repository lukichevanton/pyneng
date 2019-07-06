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

try:
   ip = input('Введите IP-сети в формате 1.0.0.255: ')
   ip1,ip2,ip3,ip4 = (ip.split('.'))
except (ValueError, TypeError):
    print("Неправильный IP-адрес")
else:  
    ip1 = int(ip1)
    ip2 = int(ip2)
    ip3 = int(ip3)
    ip4 = int(ip4)
    if ip1 <= 223 and ip1 >= 1 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print ("unicast")
    elif ip1 >= 224 and ip1 <= 239 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    elif ip1 >= 256 or ip2 >= 256 or ip3 >= 256 or ip4 >= 256:
        print("Неправильный IP-адрес")
    else:
        print("unused")