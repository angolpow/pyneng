#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


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
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                result_access[intf] = int(vlan)
            elif 'trunk allowed' in line:
                result_trunk[intf] = [ int(i) for i in line.split()[-1].split(',') ]
        return(result_access,result_trunk)

print(get_int_vlan_map('config_sw1.txt'))

