# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

"""1-ый вариант"""
while True:
    try:
        ip = input('Введите IP-сети в формате 1.0.0.255: ')
        ip1,ip2,ip3,ip4 = (ip.split('.'))
    except (ValueError, TypeError, NameError):
       print("Неправильный IP-адрес")
    else:  
        ip1 = int(ip1)
        ip2 = int(ip2)
        ip3 = int(ip3)
        ip4 = int(ip4)   
    if ip1 <= 223 and ip1 >= 1 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print ("unicast")
        break
    elif ip1 >= 224 and ip1 <= 239 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print("multicast")
        break
    elif ip == "255.255.255.255":
        print("local broadcast")
        break
    elif ip == "0.0.0.0":
        print("unassigned")
    elif ip1 >= 256 or ip2 >= 256 or ip3 >= 256 or ip4 >= 256:
        print("Неправильный IP-адрес")        
    else:
        print("unused")


"""2-ой вариант"""
while True:
    try:
        ip = input('Введите IP-сети в формате 1.0.0.255: ')
        ip1,ip2,ip3,ip4 = (ip.split('.'))
        ip1 = int(ip1)
        ip2 = int(ip2)
        ip3 = int(ip3)
        ip4 = int(ip4)
    except (ValueError, TypeError, NameError):
        print("Неправильный IP-адрес")
    else:
        ip1 = int(ip1)
        ip2 = int(ip2)
        ip3 = int(ip3)
        ip4 = int(ip4)
        if ip1 <= 223 and ip1 >= 1 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
           print("unicast")
           break
        elif ip1 >= 224 and ip1 <= 239 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
           print("multicast")
           break
        elif ip == "255.255.255.255":
            print("local broadcast")
            break
        elif ip == "0.0.0.0":
            print("unassigned")
        elif ip1 >= 256 or ip2 >= 256 or ip3 >= 256 or ip4 >= 256:
            print("Неправильный IP-адрес")        
        else:
            print("unused")