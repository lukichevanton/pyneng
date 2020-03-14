# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

r = open('sh_cdp_n_sw1.txt')
r = r.readlines()

def parse_cdp_neighbors(command_output):
    local_remote = {}
    for line in command_output:#цикл проходит по строкам
        local = []
        remote = []   
        if 'show cdp neighbors' in line:
            localdev = line.split('>')[0]   
        elif 'Eth' in line:
            remotedev, localeth, localport, *_, remoteth, remoteport = line.split()
            local.append(localdev)
            remote.append(remotedev)
            local_int = localeth + localport
            remote_int = remoteth + remoteport
            local.append(local_int)
            remote.append(remote_int)
            local_tuple = tuple(local)#делает из списка кортеж ()
            remote_tuple = tuple(remote)#делает из списка кортеж ()
            local_remote[local_tuple] = remote_tuple#добавляет кортежи в словарь
    return(local_remote)#функция возвращает значение после прохождения цикла по всем строкам
result = parse_cdp_neighbors(r)
print(result)

'''
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'), ('SW1', 'Eth0/2'): ('R2', 'Eh0/2'): ('R1', 'Eth0/0, B - Source Route Bridge\th0/0'), ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'), ('SW1', 'Eth0/5'): (th0'): ('R1', 'Eth0/0' P - P', '\nDevi    LIntrf'R6', 'Eth0/1')}
'''