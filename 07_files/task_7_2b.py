# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']

config_sw1_cleared = []

f = open('config_sw1.txt')
for line in f.read().split('\n'):        
    for item in ignore:
        if item in line:
            break
    else:
        config_sw1_cleared.append(line + '\n')
  
k = open('config_sw1_cleared.txt', 'w')
k.writelines(config_sw1_cleared)
f.close()
k.close()
