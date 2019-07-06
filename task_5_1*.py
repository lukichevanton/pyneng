#!/usr/bin/env python3


london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

""""""

#name = input("Enter device name: ")

#print(london_co[name])

""""""

#name = input("Enter device name: ")

#parameter = input("Enter parameter name: ")

#print(london_co[name][parameter])

""""""

#name = input("Enter device name: ")

#list = list(london_co[name].keys())
#list1 = ','.join(list)

#print("Enter parameter name", '(' ,list1, ")" ":", end=" ")
#parameter = input()

#print(london_co[name][parameter])

""""""

#name = input("Enter device name: ")

#list = list(london_co[name].keys())
#list1 = ','.join(list)

#print("Enter parameter name", '(' ,list1, ")", ":", end=" ")
#parameter = input()

#print(london_co[name].get(parameter, "There isn't such parameter"))


""""""

name = input("Enter device name: ")

list = list(london_co[name].keys())
list1 = ','.join(list)

print("Enter parameter name", '(' ,list1, ")", ":", end=" ")
parameter = input()

print(london_co[name].get(parameter.lower(), "There isn't such parameter"))

