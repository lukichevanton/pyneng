#!/usr/bin/env python3

from pprint import pprint
import re
import sqlite3
import yaml
import os
import sys
from tabulate import tabulate
from datetime import timedelta, datetime

''''''''''''''''''''''''''''''''''''''''''

def create_db(name, schema):
    db_exists = os.path.exists(name)
    conn = sqlite3.connect(name)
    if not db_exists:
        with open(schema, 'r') as f:
            schema = f.read()
            conn.executescript(schema)
    else:
        print('База данных существует')
    conn.close()
'''
19:45 $ python parse_dhcp_snooping.py create_db
Создаю БД dhcp_snooping.db со схемой dhcp_snooping_schema.sql
'''

''''''''''''''''''''''''''''''''''''''''''

def add_data_switches(db_file, filename):

    db_exists = os.path.exists(db_file)
    conn = sqlite3.connect(db_file)

    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать: create_db')
    elif db_exists:

        #Добавление новых данных.
        final_switches = []
        with open(filename) as f:
            templates = yaml.safe_load(f)
            for line in templates.values():
                for line2 in line.keys():
                    for line3 in line.values():
                        final2 = []
                        final2.append(line2)
                        final2.append(line3)
                        final_tuple = tuple(final2)
                        final_switches.append(final_tuple)
                #pprint(inal_switches)
        for row in final_switches:
            with conn:
                query = '''REPLACE INTO switches VALUES (?, ?)'''#самое первое добавлении данных и в случае добаления одного и того 'hostname' обновляет все значения в полях.
                conn.execute(query, row)
'''
21:04 $ python parse_dhcp_snooping.py add -s switches.yml --db dhcp_snooping.db
Добавляю данные о коммутаторах
'''

def add_data(db_file, filename):

    db_exists = os.path.exists(db_file)
    conn = sqlite3.connect(db_file)

    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать: python parse_dhcp_snooping.py create_db')
    elif db_exists:

        #Удаление данных старше 7 дней.
        now = datetime.today().replace(microsecond=0)
        week_ago = now - timedelta(days=7)
        print('\nУдаление данных старше {}...'.format(week_ago))
        with conn:          
            query = '''select * from dhcp '''
            result = conn.execute(query)
            for mac, ip, vlan, interface, switch, active, last_active in result:
                if str(last_active) < str(week_ago):
                    with conn:
                        query = '''DELETE from dhcp where last_active = last_active '''
                        result = conn.execute(query)
                        
            #Добавление новых данных.
            final_dhcp = []
            regex = re.compile(r'(?P<mac>^\S+\d+) +'
                                r'(?P<ip>\S+\d+).+snooping +'
                                r'(?P<vlan>\d+) +'
                                r'(?P<intf>\S+)')
            for line in filename:
                line_dev = line.split('_')
                with open(line) as f:
                    for line in f:
                        final2 = []
                        match = regex.search(line)
                        if match:                   
                            mac = match.group('mac')
                            ip = match.group('ip')
                            vlan = match.group('vlan')
                            intf = match.group('intf')               
                            final2.append(mac)
                            final2.append(ip)
                            final2.append(vlan)
                            final2.append(intf)
                            final2.append(line_dev[0])
                            final2_tuple = tuple(final2)
                            final_dhcp.append(final2_tuple)     
                #pprint(final_dhcp)
            with conn:
                query = '''UPDATE dhcp set active = '0' WHERE active = '1' '''
                conn.execute(query)#перед началом каждого добавления данных проставляет 0 (ноль) в поле 'active'. Таким образом можно определить активность устройств.      
            for row in final_dhcp:
                with conn:
                    query = '''REPLACE INTO dhcp VALUES (?, ?, ?, ?, ?, 1, datetime('now'))'''
                    #query = '''REPLACE INTO dhcp VALUES (?, ?, ?, ?, ?, 1, '2020-07-05 19:10:44')'''#Тестовое создание данных старше 7 дней.
                    conn.execute(query, row)#при самом первом добавлении данных проставляет 1 (один) в поле 'active' и в случае добаления одного и того 'mac' обновляет все значения в полях.
             
            with conn:              
                query = '''select * from dhcp '''
                result = conn.execute(query)
                print(tabulate(result))
'''
21:03 $ python parse_dhcp_snooping.py add sw[1-3]_dhcp_snooping.txt
Читаю информацию из файлов
sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt

Добавляю данные по DHCP записям в dhcp_snooping.db

Удаление данных старше 2020-08-01 21:04:21...
-----------------  ---------------  --  ----------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1  2020-08-08 21:04:21
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1  1  2020-08-08 21:04:21
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1  2020-08-08 21:04:21
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1  1  2020-08-08 21:04:21
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  1  2020-08-08 21:04:21
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1  2020-08-08 21:04:21
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1  2020-08-08 21:04:21
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  1  2020-08-08 21:04:21
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2  1  2020-08-08 21:04:21
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1  2020-08-08 21:04:21
-----------------  ---------------  --  ----------------  ---  -  -------------------
'''

''''''''''''''''''''''''''''''''''''''''''

def get_data(db_file, key, value):

    conn = sqlite3.connect(db_file)
    query = 'select * from dhcp where {} = ? and active = 1'.format(key)
    query2 = 'select * from dhcp where {} = ? and active = 0 '.format(key)
    result = conn.execute(query, (value, ))
    result2 = conn.execute(query2, (value, ))

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
20:07 $ python parse_dhcp_snooping.py get -k vlan -v 10
Данные из БД: dhcp_snooping.db
Информация об устройствах с такими параметрами: vlan 10

Активные записи:

-----------------  ----------  --  ---------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1  2020-08-08 19:53:12
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1  1  2020-08-08 19:53:12
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1  2020-08-08 19:53:12
-----------------  ----------  --  ---------------  ---  -  -------------------

20:11 $ python parse_dhcp_snooping.py get -k vln -v 10
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]
parse_dhcp_snooping.py get: error: argument -k: invalid choice: 'vln' (choose from 'mac', 'ip', 'vlan', 'interface', 'switch')

'''

def get_all_data(db_file):

    conn = sqlite3.connect(db_file)
    query = 'select * from dhcp where active = 1'
    query2 = 'select * from dhcp where active = 0'
    result = conn.execute(query)
    result2 = conn.execute(query2)
    
    if tabulate(result):#если в поле 'active' 1 (единица), то выводить запрос
        result = conn.execute(query)
        print('\nАктивные записи:\n')
        print(tabulate(result))
    elif not tabulate(result):#если в поле 'active' нет 1 (единицы), то не выводить запрос
        pass

    if tabulate(result2):#если в поле 'active' 0 (ноль), то выводить запрос
        result2 = conn.execute(query2)
        print('\nНеактивные записи:\n')
        print(tabulate(result2))
    elif not tabulate(result2):#если в поле 'active' нет 0 (нуля), то не выводить запрос
        pass
'''
20:10 $ python parse_dhcp_snooping.py get
В таблице dhcp такие записи:

Активные записи:

-----------------  ---------------  --  ----------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1  2020-08-08 19:53:12
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1  1  2020-08-08 19:53:12
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1  2020-08-08 19:53:12
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1  1  2020-08-08 19:53:12
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  1  2020-08-08 19:53:12
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1  2020-08-08 19:53:12
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1  2020-08-08 19:53:12
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  1  2020-08-08 19:53:12
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2  1  2020-08-08 19:53:12
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1  2020-08-08 19:53:12
-----------------  ---------------  --  ----------------  ---  -  -------------------
'''
