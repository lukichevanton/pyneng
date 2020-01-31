# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

while True:
    try:
       format = input('Введите IP-адреса в формате 10.0.1.1: ')
       ip1,ip2,ip3,ip4 = format.split('.')
    except (ValueError, TypeError, NameError):
       print("Неправильный IP-адрес")
    else:  
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
          print("Неправильный IP-адрес")
       else:
          print('unused') 
