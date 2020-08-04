#!/usr/bin/env python3

import sqlite3
import sys
from tabulate import tabulate 

db_filename = 'dhcp_snooping.db'
conn = sqlite3.connect(db_filename)

try:
	key = sys.argv[1]
	value = sys.argv[2]
	error = sys.argv[3:]
	if error:
		print('\nПожалуйста, введите два или ноль аргументов')
		'''
		$ python get_data.py ip vlan 10

		Пожалуйста, введите два или ноль аргументов
		'''
	elif not error:
		query = 'select * from dhcp where {} = ? and active = 1'.format(key)
		query2 = 'select * from dhcp where {} = ? and active = 0 '.format(key)
		result = conn.execute(query, (value, ))
		result2 = conn.execute(query2, (value, ))

		print('\nИнформация об устройствах с такими параметрами:', key, value)

		if tabulate(result):#если в поле 'active' 1 (единица), то выводить запрос
			result = conn.execute(query, (value, ))
			print('\nАктивные записи:\n')
			print(tabulate(result))
		elif not tabulate(result):#если в поле 'active' нет 1 (единицы), то не выводить запрос
			pass

		if tabulate(result2):#если в поле 'active' 0 (ноль), то выводить запрос
			result2 = conn.execute(query2, (value, ))
			print('\nНеактивные записи:\n')
			print(tabulate(result2))
		elif not tabulate(result2):#если в поле 'active' нет 0 (нуля), то не выводить запрос
			pass
		'''
		$ python get_data.py vlan 5

		Информация об устройствах с такими параметрами: vlan 5

		Активные записи:

		-----------------  ---------  -  ---------------  ---  -
		00:05:B3:7E:9B:60  10.1.5.4   5  FastEthernet0/9  sw1  1
		00:B4:A3:3E:5B:69  10.1.5.20  5  FastEthernet0/5  sw2  1
		-----------------  ---------  -  ---------------  ---  -

		Неактивные записи:

		-----------------  ---------  -  ---------------  ---  -
		00:C5:B3:7E:9B:60  10.1.5.40  5  FastEthernet0/9  sw2  0
		-----------------  ---------  -  ---------------  ---  -

		$ python get_data.py vlan 10

		Информация об устройствах с такими параметрами: vlan 10

		Активные записи:

		-----------------  ----------  --  ---------------  ---  -
		00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1
		00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/5  sw1  1
		00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1
		00:A9:33:44:A6:50  10.1.10.77  10  FastEthernet0/4  sw2  1
		-----------------  ----------  --  ---------------  ---  -
		'''
except sqlite3.OperationalError:
	print('\nДанный параметр не поддерживается.')
	print('Допустимые значения параметров: mac, ip, vlan, interface, switch, active')
	'''
	$ python get_data.py vln 10

	Данный параметр не поддерживается.
	Допустимые значения параметров: mac, ip, vlan, interface, switch, active
	'''
except IndexError:
	print('\nПожалуйста, введите два или ноль аргументов\n')
	print('Допустимые значения параметров: mac, ip, vlan, interface, switch, active')
	print('\nВ таблице dhcp такие записи:\n')
	query = 'select * from dhcp where active = 1'
	result = conn.execute(query)
	print('\nАктивные записи:\n')
	print(tabulate(result))
	query2 = 'select * from dhcp where active = 0'
	result2 = conn.execute(query2)
	print('\nНеактивные записи:\n')
	print(tabulate(result2))
	'''
	Пожалуйста, введите два или ноль аргументов

	Допустимые значения параметров: mac, ip, vlan, interface, switch, active

	В таблице dhcp такие записи:

	Активные записи:
	-----------------  ----------  --  ----------------  ---  -
	00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1   sw1  1
	00:04:A3:3E:5B:69  10.1.15.2   15  FastEthernet0/15  sw1  1
	00:05:B3:7E:9B:60  10.1.5.4     5  FastEthernet0/9   sw1  1
	00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/5   sw1  1
	00:E9:BC:3F:A6:50  100.1.1.6    3  FastEthernet0/20  sw3  1
	00:E9:22:11:A6:50  100.1.1.7    3  FastEthernet0/21  sw3  1
	00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7   sw2  1
	00:B4:A3:3E:5B:69  10.1.5.20    5  FastEthernet0/5   sw2  1
	00:A9:BC:3F:A6:50  10.1.10.65  20  FastEthernet0/2   sw2  1
	00:A9:33:44:A6:50  10.1.10.77  10  FastEthernet0/4   sw2  1
	-----------------  ----------  --  ----------------  ---  -
	Неактивные записи:
	-----------------  ---------------  -  ---------------  ---  -
	00:09:BC:3F:A6:50  192.168.100.100  1  FastEthernet0/7  sw1  0
	00:C5:B3:7E:9B:60  10.1.5.40        5  FastEthernet0/9  sw2  0
	-----------------  ---------------  -  ---------------  ---  -
	'''