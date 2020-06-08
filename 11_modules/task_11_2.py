# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

#!/usr/bin/env python3

from draw_network_graph import *

cdp = ['sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt','sh_cdp_n_r3.txt','sh_cdp_n_sw1.txt']

def create_network_map(filenames):    
    local_remote = {}
    for file in filenames:
        with open(file) as f:
            for line in f:
                local = []
                remote = []
                if 'show cdp neighbors' in line:
                    localdev = line.split('>')[0]   
                elif '/' in line:
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
    '''
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'), ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'), ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'), ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'), ('R3', 'Eth0/1'): ('R4', 'Eth0/0'), ('R3', 'Eth0/2'): ('R5', 'Eth0/0'), ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'), ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'), ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'), ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}
    '''
    local_remote2 = {} 
    key_value = []#список нужен для поиска дублированных значений в словаре
    for key, value in local_remote.items():#цикл проходит по ключам и значениям в словаре  
        if key not in key_value or value not in key_value:#если ключа или значения нет в списке, то добавляет их в список для дальнейшего поиска дублированных значений и создает словарь заново. Мы удаляем зеркальный значения/дубли.
            key_value.append(key) 
            key_value.append(value)
            local_remote2[key] = value
    return(local_remote2)#функция возвращает значение после прохождения цикла
    '''
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'), ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'), ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'), ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'), ('R3', 'Eth0/1'): ('R4', 'Eth0/0'), ('R3', 'Eth0/2'): ('R5', 'Eth0/0'), ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}
    '''
result = create_network_map(cdp)

draw_topology(result)

'''
      $ python task_11_2.py 
Graph saved in img/topology.svg
'''