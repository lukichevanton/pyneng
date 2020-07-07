# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

#!/usr/bin/env python3

import glob
sh_version_files = glob.glob("sh_vers*")#ищет все файлы в директории начинающиеся на sh_vers и передаем их функции write_inventory_to_csv в виде списка в качестве первого аргумента
print(sh_version_files)#['sh_version_r1.txt', 'sh_version_r2.txt', 'sh_version_r3.txt']

headers = ["hostname", "ios", "image", "uptime"]

from pprint import pprint
import re
import csv

def write_inventory_to_csv(data_filenames, csv_filename):
    final = []#[['hostname', 'ios', 'image', 'uptime'], ['r1', '12.4(15)T1', 'flash:c1841-advipservicesk9-mz.124-15.T1.bin', '15 days, 8 hours, 32 minutes'], ['r2', '12.4(4)T', 'disk0:c7200-js-mz.124-4.T', '45 days, 8 hours, 22 minutes'], ['r3', '12.4(4)T', 'disk0:c7200-js-mz.124-4.T', '5 days, 18 hours, 2 minutes']]
    final.append(headers)#добавляем список headers с заголовками в список final
    
    for file in data_filenames:
        file_dev = file.split('_')#разделяем имена файлов по '_', для того чтобы взять из имен названия устройств далее в скрипте
        file = open(file)
        file = file.read()#читаем файл в одну строку и передаем функции parse_sh_version

        def parse_sh_version(line):
            final2 = []#['r1', '12.4(15)T1', 'flash:c1841-advipservicesk9-mz.124-15.T1.bin', '15 days, 8 hours, 32 minutes']
            result = re.finditer(r'.+?Version (?P<ios>\S+),.+uptime is (?P<uptime>.+?)\n.+"(?P<image>\S+)"', line, re.DOTALL)#по умолчанию точка означает любой символ, кроме перевода строки, re.DOTALL изменяет это поведение и теперь в точку входит и перевод строки \n, комбинация .+ захватывает все
            for line in result:
                ios = line.group('ios')
                uptime = line.group('uptime')
                image = line.group('image')
                final2.append(file_dev[2].split('.')[0])#добавляем в список имена устройств r1, r2, r3
                final2.append(ios)
                final2.append(image)
                final2.append(uptime)
                final.append(final2)#добавляет список final2 в final
            return(final)
        result_parse = parse_sh_version(file)

    with open(csv_filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)#quoting=csv.QUOTE_NONNUMERIC - делает разделитель " кавычки
        writer.writerows(result_parse)#аналог ниже
        '''for row in data:
                writer.writerow(row)'''
    with open('routers_inventory.csv') as f:
        print(f.read())

result_csv = write_inventory_to_csv(sh_version_files, 'routers_inventory.csv')#второй аргумент это файл csv кула надо записать полученны данные
'''
['sh_version_r1.txt', 'sh_version_r3.txt', 'sh_version_r2.txt']
"hostname","ios","image","uptime"
"r1","12.4(15)T1","flash:c1841-advipservicesk9-mz.124-15.T1.bin","15 days, 8 hours, 32 minutes"
"r3","12.4(4)T","disk0:c7200-js-mz.124-4.T","5 days, 18 hours, 2 minutes"
"r2","12.4(4)T","disk0:c7200-js-mz.124-4.T","45 days, 8 hours, 22 minutes"
'''