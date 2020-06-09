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

with open('config_sw1.txt') as src, open('config_sw1_cleared.txt', 'w') as dst:
    for line in src:
        for line2 in ignore:
            if line in line2:
                break
        else:
            dst.write(line.strip())