# -*- coding: utf-8 -*-
'''
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:

    ключи: имена интерфейсов, вида „FastEthernet0/1“
    значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

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
    template = {}
    for intf, vlan in intf_vlan_mapping.items():
        template[intf] = []
        vlan = ','.join([str(vlan) for vlan in vlan])
        for line in trunk_template:            
            if line.endswith('allowed vlan'):
                template[intf].append(f'{line} {vlan}')          
            else:
                template[intf].append(line)                             
    print(template)
    return(template)
generate_trunk_config(trunk_config,trunk_mode_template)

{'FastEthernet0/1': ['switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 10,20,30'], 'FastEthernet0/2': ['switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 11,30'], 'FastEthernet0/4': ['switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 17']}
