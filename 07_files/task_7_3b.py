#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan = input()
with open('CAM_table.txt') as data:
    for string in data:
        if string.lstrip().startswith(vlan):
            line_in_list = string.strip().replace("DYNAMIC"," ").split()
            print(' {i[0]:7}{i[1]:17}{i[2]}'.format(i = line_in_list))

