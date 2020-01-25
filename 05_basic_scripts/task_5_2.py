# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#!/usr/bin/env python3

format = input('Введите IP-сеть в формате (10.1.1.0/24):  ')

ip, mask = format.split('/')

print('Network:')
print("{:8} {:8} {:8} {:8}".format(ip.split('.')[0],ip.split('.')[1],ip.split('.')[2],ip.split('.')[3]))
print("{:08b} {:08b} {:08b} {:08b}".format(int(ip.split('.')[0]),int(ip.split('.')[1]),int(ip.split('.')[2]),int(ip.split('.')[3])))
print('\n')
print('Mask')
print('/',mask)

#Далее непонятно как вычисляется:

mask_bin = ('1' * int(mask))
whilelen(mask_bin) < 32:
 mask_bin = (mask_bin + '0')
m1,m2,m3,m4 = mask_bin[0:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:32]

print('{:<10} {:<10} {:<10} {:<10}'.format((int(m1,2)) , (int(m2,2)) , (int(m3,2)) , (int(m4,2))))
print('{:<010} {:<010} {:<010} {:<010}'.format(m1,m2,m3,m4))

"""Not completed"""
