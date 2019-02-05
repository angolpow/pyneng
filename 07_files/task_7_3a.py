#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
list = []
with open('CAM_table.txt') as data:
    for string in data:
        if string.count('.') == 2: 
            line_in_list = string.strip().replace("DYNAMIC"," ").split()
            list.append(' {i[0]:7}{i[1]:17}{i[2]}'.format(i = line_in_list))
list.sort()
for line in list:
    print(line)
