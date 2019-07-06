#!/usr/bin/env python3

ip = input('введите IP-сети в формате: 10.1.1.0/24: ')

ip,mask = (ip.split('/'))
ip1,ip2,ip3,ip4 = (ip.split('.'))

print('\n' + '-' * 30)
print('Network:')
print('{:<10} {:<10} {:<10} {:<10}'.format(ip1,ip2,ip3,ip4))
print('{:<010} {:<010} {:<010} {:<010}'.format('{:b}'.format(int(ip1)) , '{:b}'.format(int(ip2)) , '{:b}'.format(int(ip3)) , '{:b}'.format(int(ip4))))

print('\n')
print('Mask:')

mask_bin = ('1' * int(mask))
whilelen(mask_bin) < 32:
 mask_bin = (mask_bin + '0')
m1,m2,m3,m4 = mask_bin[0:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:32]

print('{:<10} {:<10} {:<10} {:<10}'.format((int(m1,2)) , (int(m2,2)) , (int(m3,2)) , (int(m4,2))))
print('{:<010} {:<010} {:<010} {:<010}'.format(m1,m2,m3,m4))

""""""

from sys import argv
ip = arg[1:]

ip,mask = (ip.split('/'))
ip1,ip2,ip3,ip4 = (ip.split('.'))

print('\n' + '-' * 30)
print('Network:')
print('{:<10} {:<10} {:<10} {:<10}'.format(ip1,ip2,ip3,ip4))
print('{:<010} {:<010} {:<010} {:<010}'.format('{:b}'.format(int(ip1)) , '{:b}'.format(int(ip2)) , '{:b}'.format(int(ip3)) , '{:b}'.format(int(ip4))))

print('\n')
print('Mask:')

mask_bin = ('1' * int(mask))
whilelen(mask_bin) < 32:
 mask_bin = (mask_bin + '0')
m1,m2,m3,m4 = mask_bin[0:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:32]

print('{:<10} {:<10} {:<10} {:<10}'.format((int(m1,2)) , (int(m2,2)) , (int(m3,2)) , (int(m4,2))))
print('{:<010} {:<010} {:<010} {:<010}'.format(m1,m2,m3,m4))