# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

#!/usr/bin/env python3

from sys import argv

src = argv[1]
dst = argv[2]

f = open(' {}'.format(src))

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

k = open(' {}'.format(dst), 'w')

for line in config_sw1_cleared:
	config_sw1_cleared_txt.append(line + '\n')

k.writelines(config_sw1_cleared_txt)

f.close()
k.close()