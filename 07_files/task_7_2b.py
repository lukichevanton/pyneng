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

f = open('config_sw1.txt')

RESULT = f.read().split('\n')

ignore = ['duplex', 'alias', 'Current configuration']

config_sw1_cleared = []
config_sw1_cleared_txt = []

for command in RESULT:
    for item in ignore:
        if item in command:
            break
    else:
        print(' {}'.format(command))
        config_sw1_cleared.append(command)

k = open('config_sw1_cleared.txt', 'w')

for line in config_sw1_cleared:
	config_sw1_cleared_txt.append(line + '\n')

k.writelines(config_sw1_cleared_txt)

f.close()
k.close()