# -*- coding: utf-8 -*-

"""
Задание 22.1a

Скопировать класс Topology из задания 22.1 и изменить его.

Перенести функциональность удаления дублей в метод _normalize.
При этом метод __init__ должен выглядеть таким образом:
"""

from pprint import pprint

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

class Topology:
    def __init__(self, topology_dict):
        self.topology = topology_dict
        #self.topology = self._normalize(topology_dict)

    def topol(self):

        local_remote2 = {} 
        key_value = []#список нужен для поиска дублированных значений в словаре
        for key, value in self.topology.items():#цикл проходит по ключам и значениям в словаре  
            if key not in key_value or value not in key_value:#если ключа или значения нет в списке, то добавляет их в список для дальнейшего поиска дублированных значений и создает словарь заново. Мы удаляем зеркальный значения/дубли.
                key_value.append(key) 
                key_value.append(value)
                local_remote2[key] = value
        pprint(local_remote2)

top = Topology(topology_example)
top.topol()
'''
      $ python task_22_1a.py 
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
'''
