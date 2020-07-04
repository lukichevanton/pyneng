# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает
вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21


Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.

"""

#!/usr/bin/env python3

from pprint import pprint
import re
import csv

dhcp_snooping = ['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt','sw3_dhcp_snooping.txt']

def write_dhcp_snooping_to_csv(filenames):
    headers = ['switch','mac','ip','vlan','interface']
    final = []
    final.append(headers)
    regex = re.compile(r'(?P<mac>^\S+\d+) +'
                        r'(?P<ip>\S+\d+).+snooping +'
                        r'(?P<vlan>\d+) +'
                        r'(?P<intf>\S+)')
    for line in filenames:
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
                    final2.append(line_dev[0])
                    final2.append(mac)
                    final2.append(ip)
                    final2.append(vlan)
                    final2.append(intf)
                    final.append(final2)
    with open('sw_dhcp_snooping.csv', 'w') as f:
        writer = csv.writer(f)
        for row in final:
            writer.writerow(row)
    with open('sw_dhcp_snooping.csv') as f:
        print(f.read())   
result = write_dhcp_snooping_to_csv(dhcp_snooping)