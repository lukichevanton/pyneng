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

"""1-ый вариант"""
f = open('config_sw1.txt')
RESULT = f.read().split('\n')

ignore = ['duplex', 'alias', 'Current configuration']

for command in RESULT:
    if command.startswith('!'):
        continue
    for item in ignore:
            if item in command:
                break
    else:
        print(' {}'.format(command))

"""2-ой вариант"""
ignore = ['duplex', 'alias', 'Current configuration']
current_list = list()

with open('config_sw1.txt', 'r') as f:
    for line in f:
        line = line.rstrip()

        # Если пустая строка
        if not line:
            continue

        # Если начинается на '!'
        if line[0] == '!':
            continue

        # Если в строке есть строки из списка игнора
        found_ignore = False
        for item in ignore:
            if item in line:
                found_ignore = True
                break

        if found_ignore:
            continue

        current_list.append(line)


for line in current_list:
    print(line)
