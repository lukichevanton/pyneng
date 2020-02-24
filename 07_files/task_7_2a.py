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

f = open('config_sw1.txt')

for line in f.read().split('\n'):
    if line.startswith('!'):
        continue
    for item in ignore:
        if item in line:
            break
    else:
        print(line)
