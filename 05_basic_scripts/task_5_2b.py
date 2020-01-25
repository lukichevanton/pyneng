# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

from sys import argv
ip, mask = arg[1:]

ip,mask = (ip.split('/'))
ip1,ip2,ip3,ip4 = (ip.split('.'))

print('\n' + '-' * 30)
print('Network:')
print('{:<10} {:<10} {:<10} {:<10}'.format(ip1,ip2,ip3,ip4))
print('{:<010} {:<010} {:<010} {:<010}'.format('{:b}'.format(int(ip1)) , '{:b}'.format(int(ip2)) , '{:b}'.format(int(ip3)) , '{:b}'.format(int(ip4))))

print('\n')
print('Mask:')
print('/',mask)

#Далее непонятно как работает

mask_bin = ('1' * int(mask))
whilelen(mask_bin) < 32:
 mask_bin = (mask_bin + '0')
m1,m2,m3,m4 = mask_bin[0:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:32]

print('{:<10} {:<10} {:<10} {:<10}'.format((int(m1,2)) , (int(m2,2)) , (int(m3,2)) , (int(m4,2))))
print('{:<010} {:<010} {:<010} {:<010}'.format(m1,m2,m3,m4))

"""Not completed"""
