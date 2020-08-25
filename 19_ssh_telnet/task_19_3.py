# -*- coding: utf-8 -*-
"""
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к одному устройству, которому надо передать команды
* show - одна команда show (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции send_commands, всегда будет передаваться только один из аргументов show, config.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2

Функция возвращает строку с результатами выполнения команд или команды.

Проверить работу функции:
* со списком команд commands
* командой command

Пример работы функции:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: send_commands(r1, config=['username user5 password pass5', 'username user6 password pass6'])
Out[15]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#username user5 password pass5\nR1(config)#username user6 password pass6\nR1(config)#end\nR1#'

"""
#!/usr/bin/env python3

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"
show = command
config = commands

from pprint import pprint
import yaml
import socket
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
from task_19_1 import send_show_command
from task_19_2 import send_config_commands

def send_commands(device, com):
    #show - функция send_show_command из задания 19.1
    if com == show:
        result = send_show_command(device, com)
        return result
    #config - функция send_config_commands из задания 19.2
    elif com == config:
        result = send_config_commands(device, com)
        return result

if __name__ == "__main__":
    with open("devices2.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        result = send_commands(device, config)        
        for line in result:
            print(line)
'''
19:01 $ python task_19_3.py
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      
GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  administratively down down    
Loopback10             unassigned      YES unset  up                    up      
Connection to device timed-out: cisco_ios 192.168.100.2:22
Connection to device timed-out: cisco_ios 192.168.100.3:22

19:06 $ python task_19_3.py
config term
Enter configuration commands, one per line.  End with CNTL/Z.
csr1000v-1(config)#logging 10.255.255.1
csr1000v-1(config)#logging buffered 20010
csr1000v-1(config)#no logging console
csr1000v-1(config)#end
csr1000v-1#
Connection to device timed-out: cisco_ios 192.168.100.2:22
Connection to device timed-out: cisco_ios 192.168.100.3:22
'''