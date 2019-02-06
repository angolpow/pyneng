#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(fname):
    ''''''
    with open(fname) as file:
        result_access = {}
        result_trunk = {}
        for line in file:
            if line.startswith('interface'):
                intf = line.split()[-1]
            elif 'mode access' in line:
                result_access[intf] = 1
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                result_access[intf] = int(vlan)
            elif 'trunk allowed' in line:
                result_trunk[intf] = [ int(i) for i in line.split()[-1].split(',') ]
        return(result_access,result_trunk)

print(get_int_vlan_map('config_sw2.txt'))
