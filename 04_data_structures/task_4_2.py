# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

#!/usr/bin/env python3

mac = 'AAAA:BBBB:CCCC'

mac = mac.replace(':','.')
print(mac)

