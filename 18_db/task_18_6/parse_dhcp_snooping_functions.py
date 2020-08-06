#!/usr/bin/env python3

from pprint import pprint
import re
import sqlite3
import yaml
import glob
import os
import sys
from tabulate import tabulate
from datetime import timedelta, datetime

def create_db(name, schema):
    db_exists = os.path.exists(name)
    conn = sqlite3.connect(name)
    if not db_exists:
        with open(schema, 'r') as f:
            schema = f.read()
            conn.executescript(schema)
        print('Done')
    else:
        print('База данных существует')
    conn.close()

''''''''''''''''''''''''''''''''''''''''''

def add_data_switches(db_file, filename):

    filename = sys.argv[3]

    db_exists = os.path.exists(db_file)
    conn = sqlite3.connect(db_file)

    if not db_exists:
          print('База данных не существует. Перед добавлением данных, ее надо создать скриптом create_db.py')
    elif db_exists:
        print('\nБаза данных существует')

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
        print('Добавляю данные в таблицу switches...')
        for row in final_switches:
            with conn:
                query = '''REPLACE INTO switches VALUES (?, ?)'''#самое первое добавлении данных и в случае добаления одного и того 'hostname' обновляет все значения в полях.
                conn.execute(query, row)

''''''''''''''''''''''''''''''''''''''''''

def add_data(db_file, filename):

    #dhcp_snooping_files = glob.glob("*dhcp_snooping.txt")#файлы c данными для dhcp_snooping.db#ищет все файлы в директории заканчивающиеся на dhcp_snooping.txt
#print(dhcp_snooping_files)
    db_exists = os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    yml_filename = 'switches.yml'

    if not db_exists:
        print('База данных не существует. Перед добавлением данных, ее надо создать скриптом create_db.py')
    elif db_exists:
        print('\nБаза данных существует')
   
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
      
''''''''''''''''''''''''''''''''''''''''''

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