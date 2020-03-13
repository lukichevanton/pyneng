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

cdp = ['sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt','sh_cdp_n_r3.txt','sh_cdp_n_sw1.txt']

def create_network_map(filenames):
    local_remote = {}
    for line in filenames:#цикл проходит по строкам в списке, список состоит из имен файлов       
        line = open(line)
        line = line.readlines()
        for lines in line:#цикл проходит по строкам в списке, список это вывод команды 'show cdp neighbors'
            local = []
            remote = []
            if 'show cdp neighbors' in lines:
                localdev = lines.split('>')[0]   
            elif 'Eth' in lines:
                remotedev, localeth, localport, *_, remoteth, remoteport = lines.split()
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
result = create_network_map(cdp)
print(result)
