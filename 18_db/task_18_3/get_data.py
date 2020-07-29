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
		print('\nПожалуйста, введите два или ноль аргументов\n')
		#$ python get_data.py ip vlan 10
		#Пожалуйста, введите два или ноль аргументов
	elif not error:
		query = 'select * from dhcp where {} = ?'.format(key)
		result = conn.execute(query, (value, ))
		print('\nИнформация об устройствах с такими параметрами:', key, value)
		print(tabulate(result))
		#$ python get_data.py vlan 10
		#Информация об устройствах с такими параметрами: vlan 10
		#-----------------  ----------  --  ---------------  ---
		#00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1
except sqlite3.OperationalError:
	print('\nДанный параметр не поддерживается.')
	print('Допустимые значения параметров: mac, ip, vlan, interface, switch\n')
	#$ python get_data.py vln 10
	#Данный параметр не поддерживается.
	#Допустимые значения параметров: mac, ip, vlan, interface, switch
except IndexError:
	print('\nПожалуйста, введите два или ноль аргументов\n')
	query = 'select * from dhcp'
	result = conn.execute(query)
	print('\nВ таблице dhcp такие записи:\n')
	print(tabulate(result))
	#$ python get_data.py ip vlan 10
	#Пожалуйста, введите два или ноль аргументов
	#В таблице dhcp такие записи:
	#-----------------  ---------------  --  ----------------  ---
	#00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1
	#00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1
	#00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1
	#00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1
	
	


