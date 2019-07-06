"""
Задание 6.1

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.

Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в новый список mac_cisco

Ограничение: Все задания надо выполнять используя только пройденные темы.

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
"""

"""
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []

for macs in mac:
    mac_cisco.append(macs.replace(':','.'))
print(mac_cisco)
"""

"""
Задание 6.2

    Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
    Определить тип IP-адреса.
    В зависимости от типа адреса, вывести на стандартный поток вывода:
        „unicast“ - если первый байт в диапазоне 1-223
        „multicast“ - если первый байт в диапазоне 224-239
        „local broadcast“ - если IP-адрес равен 255.255.255.255
        „unassigned“ - если IP-адрес равен 0.0.0.0
        „unused“ - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

"""1-ый вариант
ip = input('введите IP-сети в формате 10.0.1.1: ')
ip1,ip2,ip3,ip4 = (ip.split('.'))
ip1 = int(ip1)
ip2 = int(ip2)
ip3 = int(ip3)
ip4 = int(ip4)

if ip1 <= 223 and ip1 >= 1:
    print ("unicast")
elif ip1 >= 224 and ip1 <= 239:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")

"""

"""2-ой вариант
try:
   ip = input('Введите IP-сети в формате 1.0.0.255: ')
   ip1,ip2,ip3,ip4 = (ip.split('.'))
except (ValueError, TypeError):
    print("unused")
else:  
    ip1 = int(ip1)
    ip2 = int(ip2)
    ip3 = int(ip3)
    ip4 = int(ip4)
    if ip1 <= 223 and ip1 >= 1 :
        print ("unicast")
    elif ip1 >= 224 and ip1 <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
"""

"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:

    состоит из 4 чисел разделенных точкой,
    каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес“

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

"""
try:
   ip = input('Введите IP-сети в формате 1.0.0.255: ')
   ip1,ip2,ip3,ip4 = (ip.split('.'))
except (ValueError, TypeError):
    print("Неправильный IP-адрес")
else:  
    ip1 = int(ip1)
    ip2 = int(ip2)
    ip3 = int(ip3)
    ip4 = int(ip4)
    if ip1 <= 223 and ip1 >= 1 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print ("unicast")
    elif ip1 >= 224 and ip1 <= 239 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    elif ip1 >= 256 or ip2 >= 256 or ip3 >= 256 or ip4 >= 256:
        print("Неправильный IP-адрес")
    else:
        print("unused")
"""

"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

"""1-ый вариант
while True:
    try:
        ip = input('Введите IP-сети в формате 1.0.0.255: ')
        ip1,ip2,ip3,ip4 = (ip.split('.'))
    except (ValueError, TypeError, NameError):
       print("Неправильный IP-адрес")
    else:  
        ip1 = int(ip1)
        ip2 = int(ip2)
        ip3 = int(ip3)
        ip4 = int(ip4)   
    if ip1 <= 223 and ip1 >= 1 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print ("unicast")
        break
    elif ip1 >= 224 and ip1 <= 239 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
        print("multicast")
        break
    elif ip == "255.255.255.255":
        print("local broadcast")
        break
    elif ip == "0.0.0.0":
        print("unassigned")
    elif ip1 >= 256 or ip2 >= 256 or ip3 >= 256 or ip4 >= 256:
        print("Неправильный IP-адрес")        
    else:
        print("unused")
"""

"""2-ой вариант
while True:
    try:
        ip = input('Введите IP-сети в формате 1.0.0.255: ')
        ip1,ip2,ip3,ip4 = (ip.split('.'))
        ip1 = int(ip1)
        ip2 = int(ip2)
        ip3 = int(ip3)
        ip4 = int(ip4)
    except (ValueError, TypeError, NameError):
        print("Неправильный IP-адрес")
    else:
        ip1 = int(ip1)
        ip2 = int(ip2)
        ip3 = int(ip3)
        ip4 = int(ip4)
        if ip1 <= 223 and ip1 >= 1 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
           print("unicast")
           break
        elif ip1 >= 224 and ip1 <= 239 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
           print("multicast")
           break
        elif ip == "255.255.255.255":
            print("local broadcast")
            break
        elif ip == "0.0.0.0":
            print("unassigned")
        elif ip1 >= 256 or ip2 >= 256 or ip3 >= 256 or ip4 >= 256:
            print("Неправильный IP-адрес")        
        else:
            print("unused")
"""

"""Задание 6.3

В скрипте сделан генератор конфигурации для access-портов.

Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать, что с ним делать.

Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка указывает как воспринимать номера VLAN, которые идут дальше:

    add - VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
    del - VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
    only - на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)

Задача для портов 0/1, 0/2, 0/4:

    сгенерировать конфигурацию на основе шаблона trunk_template
    с учетом ключевых слов add, del, only

Код не должен привязываться к конкретным номерам портов. То есть, если в словаре trunk будут другие номера интерфейсов, код должен работать.

Ограничение: Все задания надо выполнять используя только пройденные темы.

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}

for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
       if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))
"""

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

trunk = {
        '0/1': ['add', '10', '20'],#switchport trunk allowed vlan add
        '0/2': ['only', '11', '30'],#switchport trunk allowed vlan
        '0/4': ['del', '17']#switchport trunk allowed vlan remove
    }

for intf, vlan in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('vlan'):
            print(' {} {} {}'.format(command, vlan[0].replace('only','').replace('del','remove '), ','.join(vlan[1::])))
        else:
            print(' {}'.format(command))
