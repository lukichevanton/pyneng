# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 20.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве с помощью netmiko.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает метод netmiko send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
"""
import yaml
from jinja2 import Environment, FileSystemLoader
import socket
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

data = {
    "tun_num": None,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}

src_device_params = {'device_type': 'cisco_ios',
                'ip': '192.168.100.1',
                'username': 'user',
                'password': 'userpass',
                'secret': 'enablepass',
                'port': 22,
                 }
dst_device_params = {'device_type': 'cisco_ios',
                'ip': '192.168.100.2',
                'username': 'user',
                'password': 'userpass',
                'secret': 'enablepass',
                'port': 22,
                 }

def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
	
	src_template = src_template.split('/')
	env = Environment(loader=FileSystemLoader(src_template[0]))
	src_template = env.get_template(src_template[1])
	src_template = src_template.render(vpn_data_dict)

	dst_template = dst_template.split('/')
	env = Environment(loader=FileSystemLoader(dst_template[0]))
	dst_template = env.get_template(dst_template[1])
	dst_template = dst_template.render(vpn_data_dict)

	result = []
	try:
		with ConnectHandler(**src_device_params) as ssh:
			ssh.enable()
			output = ssh.send_config_set(src_template)
			result.append(output)
	except (NetMikoAuthenticationException, NetMikoTimeoutException, socket.timeout) as error:
		print(error)

	try:
		with ConnectHandler(**dst_device_params) as ssh:
			ssh.enable()
			output = ssh.send_config_set(dst_template)
			result.append(output)
	except (NetMikoAuthenticationException, NetMikoTimeoutException, socket.timeout) as error:
		print(error)

	return result
		
# так должен выглядеть вызов функции
if __name__ == "__main__":

	src_template = "templates/gre_ipsec_vpn_1.txt"
	dst_template = "templates/gre_ipsec_vpn_2.txt"
	
	result = configure_vpn(src_device_params, dst_device_params, src_template, dst_template, data)
	for line in result:
		print(line)