# -*- coding: utf-8 -*-
"""
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})
"""
#!/usr/bin/env python3

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]
ignore = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']

commands = commands_with_errors + correct_commands

from pprint import pprint
import re
import yaml
import socket
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

#'log' контролирует будет ли выводится на стандартный поток вывода информация о том к какому устройству выполняется подключение
def send_config_commands(device, config_commands, log=True):

    regex = re.compile(r'.*% (?P<error>.*)')
    result_good = {}#первый словарь с выводом команд, которые выполнились без ошибки
    result_bad = {}#второй словарь с выводом команд, которые выполнились с ошибками

    try:
    	#'log' контролирует будет ли выводится на стандартный поток вывода информация о том к какому устройству выполняется подключение
        if log:
            print('Подключаюсь к {}...'.format(device['host']))
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for com in config_commands:
                output = ssh.send_config_set(com)
                if ignore_command(output, ignore):
                    final = regex.search(output)
                    if final:
                        error = final.group('error')
                        print('Команда "{}" выполнилась с ошибкой "{}" на устройстве {}'.format(com, error, device['host']))
                        #Варианты ответа [y]/n:
                        errcom = input('Продолжать выполнять команды? [y]/n:')
                        #y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
                        #второй словарь с выводом команд, которые выполнились с ошибками
                        if not errcom:
                        	result_bad[com] = output
                        elif 'y' in errcom:
                        	result_bad[com] = output
                        elif 'n' or 'no' not in errcom:
                        	result_bad[com] = output
                        #n или no - не выполнять остальные команды
                        elif 'n' or 'no' in errcom:
                        	pass
                else:
                	#первый словарь с выводом команд, которые выполнились без ошибки
                    result_good[com] = output
        return result_good, result_bad
    except (NetMikoAuthenticationException, NetMikoTimeoutException, socket.timeout) as error:
        #'log' контролирует будет ли выводится на стандартный поток вывода информация о том к какому устройству выполняется подключение
        if log:
            print(error)

if __name__ == "__main__":
    with open("devices2.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        result = send_config_commands(device, commands)      
        '''
        pprint(result)
        try:
            good, bad = result
            print(bad.keys())
        except TypeError:
            pass
        '''
'''
19:39 $ python task_19_2c.py
Подключаюсь к ios-xe-mgmt-latest.cisco.com...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве ios-xe-mgmt-latest.cisco.com
Продолжать выполнять команды? [y]/n:y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве ios-xe-mgmt-latest.cisco.com
Продолжать выполнять команды? [y]/n:y
Команда "a" выполнилась с ошибкой "Ambiguous command:  "a"" на устройстве ios-xe-mgmt-latest.cisco.com
Продолжать выполнять команды? [y]/n:y
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with '
                    'CNTL/Z.\n'
                    'csr1000v-1(config)#ip http server\n'
                    'csr1000v-1(config)#end\n'
                    'csr1000v-1#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End '
                            'with CNTL/Z.\n'
                            'csr1000v-1(config)#logging buffered 20010\n'
                            'csr1000v-1(config)#end\n'
                            'csr1000v-1#'},
 {'a': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'csr1000v-1(config)#a\n'
       '% Ambiguous command:  "a"\n'
       'csr1000v-1(config)#end\n'
       'csr1000v-1#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'csr1000v-1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'csr1000v-1(config)#end\n'
             'csr1000v-1#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'csr1000v-1(config)#logging 0255.255.1\n'
                        '                           ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'csr1000v-1(config)#end\n'
                        'csr1000v-1#'})
dict_keys(['logging 0255.255.1', 'logging', 'a'])
Подключаюсь к 192.168.100.2...
Connection to device timed-out: cisco_ios 192.168.100.2:22
None
Подключаюсь к 192.168.100.3...
Connection to device timed-out: cisco_ios 192.168.100.3:22
None

19:43 $ python task_19_2c.py
Подключаюсь к ios-xe-mgmt-latest.cisco.com...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве ios-xe-mgmt-latest.cisco.com
Продолжать выполнять команды? [y]/n:n
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве ios-xe-mgmt-latest.cisco.com
Продолжать выполнять команды? [y]/n:n
Команда "a" выполнилась с ошибкой "Ambiguous command:  "a"" на устройстве ios-xe-mgmt-latest.cisco.com
Продолжать выполнять команды? [y]/n:n
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with '
                    'CNTL/Z.\n'
                    'csr1000v-1(config)#ip http server\n'
                    'csr1000v-1(config)#end\n'
                    'csr1000v-1#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End '
                            'with CNTL/Z.\n'
                            'csr1000v-1(config)#logging buffered 20010\n'
                            'csr1000v-1(config)#end\n'
                            'csr1000v-1#'},
 {})
dict_keys([])
Подключаюсь к 192.168.100.2...
Connection to device timed-out: cisco_ios 192.168.100.2:22
None
Подключаюсь к 192.168.100.3...
Connection to device timed-out: cisco_ios 192.168.100.3:22
None
'''