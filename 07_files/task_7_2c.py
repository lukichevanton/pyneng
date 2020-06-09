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

#!/usr/bin/env python3

from sys import argv

src_file, dst_file = argv[1:]

ignore = ['duplex', 'alias', 'Current configuration']

with open(src_file) as src, open(dst_file, 'w') as dst:      
    for line in src:
        for line2 in ignore:
            if line2 in line:
                break 
        else:
            dst.write(line.strip())
