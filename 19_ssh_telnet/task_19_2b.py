# -*- coding: utf-8 -*-
"""
Задание 19.2b

Скопировать функцию send_config_commands из задания 19.2a и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве, например:
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1

Ошибки должны выводиться всегда, независимо от значения параметра log.
При этом, параметр log по-прежнему должен контролировать будет ли выводиться сообщение:
Подключаюсь к 192.168.100.1...


Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.


Пример работы функции send_config_commands:

In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'a',
 'logging buffered 20010',
 'ip http server']

In [17]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Команда "a" выполнилась с ошибкой "Ambiguous command:  "a"" на устройстве 192.168.100.1

In [18]: pprint(result, width=120)
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                    'R1(config)#ip http server\n'
                    'R1(config)#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                            'R1(config)#logging buffered 20010\n'
                            'R1(config)#'},
 {'a': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'R1(config)#a\n'
       '% Ambiguous command:  "a"\n'
       'R1(config)#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

In [19]: good, bad = result

In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])

In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'a'])


Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
"""
#!/usr/bin/env python3

# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]
ignore = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']

commands = commands_with_errors + correct_commands

import yaml
from pprint import pprint
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetmikoAuthenticationException

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

def send_config_commands(device, config_commands, log=False):
    result = []
    result_good = []
    result_bad = []
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(config_commands)
            result.append(output)
            if log:
                for line in result:
                    print(line)
    except (NetMikoTimeoutException, NetmikoAuthenticationException) as error:
        if log:
            print(error)
            
    for line in result:
        for 
        if ignore_command(line, ignore):
            result_bad.append(output)
        else:
            result_good.append(output)
    print(result)
    print(result_error)
    return result, result_error
		
if __name__ == "__main__":
	with open("devices2.yaml") as f:
		devices = yaml.safe_load(f)
	for device in devices:
		final = send_config_commands(device, commands)