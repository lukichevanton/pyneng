# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']

with open('config_sw1.txt', 'r') as f:
    for line in f:
        if line.startswith('!'):
            continue
        for line2 in ignore:
            if line in line2:
                break
        else:
            print(line.strip())
