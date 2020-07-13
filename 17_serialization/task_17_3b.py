# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

#!/usr/bin/env python3

from draw_network_graph import *
from pprint import pprint
import yaml

def transform_topology(file_yaml):
    local_remote = {}
    with open(file_yaml) as f:    
        templates = yaml.safe_load(f)
        for key1, value1 in templates.items():
            for key2, value2 in value1.items():
                local = []
                remote = []
                local.append(key1)
                local.append(key2)
                for key3, value3 in value2.items():
                    remote.append(key3)
                    remote.append(value3)
                local_tuple = tuple(local)
                remote_tuple = tuple(remote)
                local_remote[local_tuple] = remote_tuple
    '''
    {('R1', 'Eth 0/0'): ('SW1', 'Eth 0/1'),
    ('R2', 'Eth 0/0'): ('SW1', 'Eth 0/2'),
    ('R2', 'Eth 0/1'): ('R5', 'Eth 0/0'),
    ('R2', 'Eth 0/2'): ('R6', 'Eth 0/1'),
    ('R3', 'Eth 0/0'): ('SW1', 'Eth 0/3'),
    ('R4', 'Eth 0/0'): ('SW1', 'Eth 0/4'),
    ('R4', 'Eth 0/1'): ('R5', 'Eth 0/1'),
    ('R5', 'Eth 0/0'): ('R2', 'Eth 0/1'),
    ('R5', 'Eth 0/1'): ('R4', 'Eth 0/1'),
    ('R6', 'Eth 0/1'): ('R2', 'Eth 0/2'),
    ('SW1', 'Eth 0/1'): ('R1', 'Eth 0/0'),
    ('SW1', 'Eth 0/2'): ('R2', 'Eth 0/0'),
    ('SW1', 'Eth 0/3'): ('R3', 'Eth 0/0'),
    ('SW1', 'Eth 0/4'): ('R4', 'Eth 0/0')}
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
    {('R1', 'Eth 0/0'): ('SW1', 'Eth 0/1'), ('R2', 'Eth 0/0'): ('SW1', 'Eth 0/2'), ('R2', 'Eth 0/1'): ('R5', 'Eth 0/0'), ('R2', 'Eth 0/2'): ('R6', 'Eth 0/1'), ('R3', 'Eth 0/0'): ('SW1', 'Eth 0/3'), ('R4', 'Eth 0/0'): ('SW1', 'Eth 0/4'), ('R4', 'Eth 0/1'): ('R5', 'Eth 0/1')}
    '''
result = transform_topology('topology.yaml')

draw_topology(result)