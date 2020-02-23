# -*- coding: utf-8 -*-
'''
Задание 9.2

Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

У функции должны быть такие параметры:

    intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:

{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

    trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_mode_template. В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_config.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):   
    template = []
    for intf, vlan in intf_vlan_mapping.items():
        vlan = ','.join([str(vlan) for vlan in vlan])
        template.append('interface ' + intf)
        for line in trunk_template:            
            if line.endswith('allowed vlan'):
                template.append(f'{line} {vlan}')   
            else:
                template.append(f'{line}')                         
    print(template)
    rerurn(template)    
generate_trunk_config(trunk_config,trunk_mode_template)

['interface FastEthernet0/1', 'switchport mode trunk', 'switchport trunknative vlan 999', 'switchport trunk allowed vlan 10,20,30', 'interface FastEthernet0/2', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 11,30', 'interface FastEthernet0/4', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 17']
