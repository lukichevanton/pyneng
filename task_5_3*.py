#!/usr/bin/env python3

# access template
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

# trunk template
trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

mode = input("Enter interface mode (access/trunk): ")

type = input("Enter interface type and number: ")

vlans = input("Enter vlan(s): ")


print('interface {}'.format(type))


print('\n'.join(access_template).format(vlans))
print('\n'.join(trunk_template).format(vlans))


