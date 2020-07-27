#!/usr/bin/env python3

from pprint import pprint
import sqlite3
import sys
from tabulate import tabulate 

#key, value = sys.argv[1:]
#keys = ['mac', 'ip', 'vlan', 'interface']
#keys.remove(key)

db_filename = 'dhcp_snooping.db'
conn = sqlite3.connect(db_filename)

#Позволяет далее обращаться к данным в колонках, по имени колонки
#conn.row_factory = sqlite3.Row

try:
	key, value = sys.argv[1:]
	query = 'select * from dhcp where {} = ?'.format(key)
	result = conn.execute(query, (value, ))
	print('\nИнформация об устройствах с такими параметрами:', key, value)
	print(tabulate(result))
except sqlite3.OperationalError:
	print('\nДанный параметр не поддерживается.')
	print('Допустимые значения параметров: mac, ip, vlan, interface, switch\n')
except ValueError:
	print('\nПожалуйста, введите два или ноль аргументов\n')
	query = 'select * from dhcp'
	result = conn.execute(query)
	print('\nВ таблице dhcp такие записи:\n')
	print(tabulate(result))


'''
Скрипту могут передаваться аргументы и, в зависимости от аргументов, надо выводить разную информацию.
Если скрипт вызван:
* без аргументов, вывести всё содержимое таблицы dhcp
* с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
* с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов

Примеры вывода для разного количества и значений аргументов:

$ python get_data.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch

$ python get_data.py ip vlan 10
Пожалуйста, введите два или ноль аргументов
'''