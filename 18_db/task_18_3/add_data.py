#!/usr/bin/env python3

from pprint import pprint
import re
import sqlite3
import yaml
import glob
import os

dhcp_snooping_files = glob.glob("*dhcp_snooping.txt")#файлы c данными для dhcp_snooping.db#ищет все файлы в директории заканчивающиеся на dhcp_snooping.txt
#print(dhcp_snooping_files)
yml_filename = 'switches.yml'#файл c данными для dhcp_snooping.db

db_filename = 'dhcp_snooping.db'#файл bd с данными из switches.yml и файлов *dhcp_snooping.txt
db_exists = os.path.exists(db_filename)

if not db_exists:
    print('База данных не существует. Перед добавлением данных, ее надо создать скриптом create_db.py')
elif db_exists:
    print('База данных существует')

    conn = sqlite3.connect(db_filename)

    def switches_dhcp(switches, dhcp):

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
        #pprint(final_switches)

        print('Добавляю данные в таблицу switches...')
        for row in final_switches:
            try:
                with conn:
                    query = '''insert into switches (hostname, location) values (?, ?)'''
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print('При добавлении данных: {} Возникла ошибка:'.format(row), e)
    
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
        for row in final_dhcp:
            try:
                with conn:
                    query = '''insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print('При добавлении данных: {} Возникла ошибка:'.format(row), e)
        conn.close()
    switches_dhcp(yml_filename, dhcp_snooping_files)
'''
База данных не существует. Перед добавлением данных, ее надо 
создать скриптом create_db.py

База данных существует
Добавляю данные в таблицу switches...
Добавляю данные в таблицу dhcp...

База данных существует
Добавляю данные в таблицу switches...
При добавлении данных: ('sw1', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
При добавлении данных: ('sw2', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
При добавлении данных: ('sw3', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
Добавляю данные в таблицу dhcp...
При добавлении данных: ('00:09:BB:3D:D6:58', '10.1.10.2', '10', 'FastEthernet0/1', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:04:A3:3E:5B:69', '10.1.5.2', '5', 'FastEthernet0/10', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:05:B3:7E:9B:60', '10.1.5.4', '5', 'FastEthernet0/9', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
'''
