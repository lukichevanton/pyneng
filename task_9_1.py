# -*- coding: utf-8 -*-
'''
Задание 9.1
Создать функцию, которая генерирует конфигурацию для access-портов.
Функция ожидает такие аргументы:
- словарь с соответствием интерфейс-VLAN такого вида:
    {'FastEthernet0/12':10,
     'FastEthernet0/14':11,
     'FastEthernet0/16':17}
- шаблон конфигурации access-портов в виде списка команд (список access_mode_template)
Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template.
В конце строк в списке не должно быть символа перевода строки.
В этом задании заготовка для функции уже сделана и надо только продолжить писать само тело функции.
Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
Проверить работу функции на примере словаря access_config.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def generate_access_config(intf_vlan_mapping, access_template):
    template = []
    for intf, vlan in intf_vlan_mapping.items():
        template.append('interface ' + intf)
        for line in access_template:
            if line.endswith('access vlan'):
                template.append(f'{line} {vlan}')
            else:
                template.append(f'{line}')         
    print(template)
  
generate_access_config(access_config,access_mode_template)
