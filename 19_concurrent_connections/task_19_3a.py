# -*- coding: utf-8 -*-
"""
Задание 19.3a

Создать функцию send_command_to_devices, которая отправляет
список указанных команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какие команды. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом каждой команды надо написать имя хоста и саму команду):

R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          87   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R1#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300
Internet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
R3#sh ip route | ex -

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O        10.1.1.1/32 [110/11] via 192.168.100.1, 07:12:03, Ethernet0/0
O        10.30.0.0/24 [110/20] via 192.168.100.1, 07:12:03, Ethernet0/0


Порядок команд в файле может быть любым.

Для выполнения задания можно создавать любые дополнительные функции, а также использовать функции созданные в предыдущих заданиях.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""

# Этот словарь нужен только для проверки работа кода, в нем можно менять IP-адреса
# тест берет адреса из файла devices.yaml

commands = {
    "192.168.100.3": ["sh ip int br", "sh ip route | ex -"],
    "ios-xe-mgmt.cisco.com": ["sh int desc", "sh ip int br"],
    "192.168.100.2": ["sh int desc"]
}

from datetime import datetime
import time
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor
import logging
from pprint import pprint

import netmiko
import yaml

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

def send_show_command_to_devices(device, command):
	final = []
	start_msg = '===> {} Connection: {}'
	received_msg = '<=== {} Received:   {}'
	ip = device['host']
	if commands.get(device['host']):
		command = commands[device['host']]
	logging.info(start_msg.format(datetime.now().time(), ip))

	with netmiko.ConnectHandler(**device) as ssh:
		ssh.enable()	
		output1 = ssh.send_command(strip_command=False, command_string=command[0])
		final.append(device['host']+'#'+output1+'\n')
		output2 = ssh.send_command(strip_command=False, command_string=command[1])
		final.append(device['host']+'#'+output2+'\n')
		logging.info(received_msg.format(datetime.now().time(), ip))
	return final

with open('devices2.yaml') as f:
	devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
	result = executor.map(send_show_command_to_devices, devices, commands)
	for output in result:
		pprint(output)
		f = open('show.txt', 'a')
		for line in output:
			f.write(line)
'''
ios-xe-mgmt.cisco.com#sh int desc
Interface                      Status         Protocol Description
Gi1                            up             up       MANAGEMENT INTERFACE - DON'T TOUCH ME
Gi2                            admin down     down     Network Interface
Gi3                            admin down     down     Network Interface
Lo15                           up             up       Added By KaussezPausies
Lo100                          up             up       Added By KaussezPausies
ios-xe-mgmt.cisco.com#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      
GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  administratively down down    
Loopback15             unassigned      YES unset  up                    up      
Loopback100            172.16.55.1     YES other  up                    up      
'''