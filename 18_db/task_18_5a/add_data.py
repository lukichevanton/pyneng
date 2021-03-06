#!/usr/bin/env python3

from pprint import pprint
import re
import sqlite3
import yaml
import glob
import os
from tabulate import tabulate
from datetime import timedelta, datetime

dhcp_snooping_files = glob.glob("*dhcp_snooping.txt")#файлы c данными для dhcp_snooping.db#ищет все файлы в директории заканчивающиеся на dhcp_snooping.txt
#print(dhcp_snooping_files)
yml_filename = 'switches.yml'#файл c данными для dhcp_snooping.db
db_filename = 'dhcp_snooping.db'#файл bd с данными из switches.yml и файлов *dhcp_snooping.txt
db_exists = os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
'''
from datetime import timedelta, datetime
now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days=7)
print(now)
print(week_ago)
print(now > week_ago)
print(str(now) > str(week_ago))
'''
def switches_dhcp(switches, dhcp):
    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать скриптом create_db.py')
    elif db_exists:
        print('База данных существует')

        #Удаление данных старше 7 дней.
        now = datetime.today().replace(microsecond=0)
        week_ago = now - timedelta(days=7)
        print('Удаление данных старше {}...'.format(week_ago))
        with conn:          
            query = '''select * from dhcp '''
            result = conn.execute(query)
            for mac, ip, vlan, interface, switch, active, last_active in result:
                if str(last_active) < str(week_ago):
                    with conn:
                        query = '''DELETE from dhcp where last_active = last_active '''
                        result = conn.execute(query)

        #Добавление новых данных.
        final_switches = []
        with open(switches) as f:
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
        print('Добавляю данные в таблицу switches...')
        for row in final_switches:
            with conn:
                query = '''REPLACE INTO switches VALUES (?, ?)'''#самое первое добавлении данных и в случае добаления одного и того 'hostname' обновляет все значения в полях.
                conn.execute(query, row)
                
        #Добавление новых данных.
        final_dhcp = []
        regex = re.compile(r'(?P<mac>^\S+\d+) +'
                                r'(?P<ip>\S+\d+).+snooping +'
                                r'(?P<vlan>\d+) +'
                                r'(?P<intf>\S+)')
        for line in dhcp:
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
        print('Добавляю данные в таблицу dhcp...')
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
        conn.close()
        
switches_dhcp(yml_filename, dhcp_snooping_files)
'''
21:13 $ python add_data.py 
База данных существует
Удаление данных старше 2020-07-29 21:07:59...
Добавляю данные в таблицу switches...
Добавляю данные в таблицу dhcp...
-----------------  ---------------  --  ----------------  ---  -  -------------------
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  0  2020-07-05 19:10:44
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  0  2020-07-05 19:10:44
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1  2020-08-05 21:13:23
00:04:A3:3E:5B:69  10.1.15.2        15  FastEthernet0/15  sw1  1  2020-08-05 21:13:23
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1  2020-08-05 21:13:23
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/5   sw1  1  2020-08-05 21:13:23
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1  2020-08-05 21:13:23
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3  1  2020-08-05 21:13:23
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1  2020-08-05 21:13:23
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1  2020-08-05 21:13:23
00:A9:BC:3F:A6:50  10.1.10.65       20  FastEthernet0/2   sw2  1  2020-08-05 21:13:23
00:A9:33:44:A6:50  10.1.10.77       10  FastEthernet0/4   sw2  1  2020-08-05 21:13:23
-----------------  ---------------  --  ----------------  ---  -  -------------------

21:17 $ python add_data.py 
База данных существует
Удаление данных старше 2020-07-29 21:18:01...
Добавляю данные в таблицу switches...
Добавляю данные в таблицу dhcp...
-----------------  ----------  --  ----------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1   sw1  1  2020-08-05 21:18:01
00:04:A3:3E:5B:69  10.1.15.2   15  FastEthernet0/15  sw1  1  2020-08-05 21:18:01
00:05:B3:7E:9B:60  10.1.5.4     5  FastEthernet0/9   sw1  1  2020-08-05 21:18:01
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/5   sw1  1  2020-08-05 21:18:01
00:E9:BC:3F:A6:50  100.1.1.6    3  FastEthernet0/20  sw3  1  2020-08-05 21:18:01
00:E9:22:11:A6:50  100.1.1.7    3  FastEthernet0/21  sw3  1  2020-08-05 21:18:01
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7   sw2  1  2020-08-05 21:18:01
00:B4:A3:3E:5B:69  10.1.5.20    5  FastEthernet0/5   sw2  1  2020-08-05 21:18:01
00:A9:BC:3F:A6:50  10.1.10.65  20  FastEthernet0/2   sw2  1  2020-08-05 21:18:01
00:A9:33:44:A6:50  10.1.10.77  10  FastEthernet0/4   sw2  1  2020-08-05 21:18:01
-----------------  ----------  --  ----------------  ---  -  -------------------
'''