# -*- coding: utf-8 -*-
"""
Задание 19.4

Создать функцию send_commands_to_devices, которая отправляет команду show или config на разные устройства в параллельных потоках, а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* show - команда show, которую нужно отправить (по умолчанию, значение None)
* config - команды конфигурационного режима, которые нужно отправить (по умолчанию, значение None)
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Пример вызова функции:
In [5]: send_commands_to_devices(devices, show='sh clock', filename='result.txt')

In [6]: cat result.txt
R1#sh clock
*04:56:34.668 UTC Sat Mar 23 2019
R2#sh clock
*04:56:34.687 UTC Sat Mar 23 2019
R3#sh clock
*04:56:40.354 UTC Sat Mar 23 2019

In [11]: send_commands_to_devices(devices, config='logging 10.5.5.5', filename='result.txt')

In [12]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.5.5.5
R1(config)#end
R1#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#logging 10.5.5.5
R2(config)#end
R2#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#logging 10.5.5.5
R3(config)#end
R3#

In [13]: send_commands_to_devices(devices,
                                  config=['router ospf 55', 'network 0.0.0.0 255.255.255.255 area 0'],
                                  filename='result.txt')

In [14]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#router ospf 55
R1(config-router)#network 0.0.0.0 255.255.255.255 area 0
R1(config-router)#end
R1#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#router ospf 55
R2(config-router)#network 0.0.0.0 255.255.255.255 area 0
R2(config-router)#end
R2#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#router ospf 55
R3(config-router)#network 0.0.0.0 255.255.255.255 area 0
R3(config-router)#end
R3#


Для выполнения задания можно создавать любые дополнительные функции.
"""

from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

import netmiko
import yaml

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

def send_commands_to_devices(device, filename, show=None, config=None):

	final = []
	start_msg = '===> {} Connection: {}'
	received_msg = '<=== {} Received:   {}'
	ip = device['host']

	logging.info(start_msg.format(datetime.now().time(), ip))

	with netmiko.ConnectHandler(**device) as ssh:
		ssh.enable()
		if show != None:
			output = ssh.send_command(strip_command=False, command_string=show)
			final.append('\n'+device['host']+'#'+output)
		elif config != None:
			output = ssh.send_config_set(config)
			final.append('\n'+device['host']+'#'+'\n'+output)
		logging.info(received_msg.format(datetime.now().time(), ip))
	with open(filename, 'a') as f:
		for line in final:
			f.write(line)
	return final

with open('test_devices.yaml') as f:
	devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
	future_list = []
	for device in devices:
		future = executor.submit(send_commands_to_devices, device, show='sh clock', filename='result.txt')
		#future = executor.submit(send_commands_to_devices, device, config='logging 10.5.5.5', filename='result.txt')
		#future = executor.submit(send_commands_to_devices, device, config=['router ospf 55', 'network 0.0.0.0 255.255.255.255 area 0'], filename='result.txt')
		future_list.append(future)
	# то же самое в виде list comprehensions:
	# future_list = [executor.submit(send_show, device, 'sh clock') for device in devices]
	for f in as_completed(future_list):
		for f in f.result():
			print(f)
'''
ios-xe-mgmt.cisco.com#sh clock
*20:02:04.955 UTC Wed Nov 4 2020
ios-xe-mgmt.cisco.com#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v(config)#logging 10.5.5.5
csr1000v(config)#end
csr1000v#
ios-xe-mgmt.cisco.com#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v(config)#router ospf 55
csr1000v(config-router)#network 0.0.0.0 255.255.255.255 area 0
csr1000v(config-router)#end
csr1000v#
'''