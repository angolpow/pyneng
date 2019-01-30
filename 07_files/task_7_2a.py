#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

file = open(argv[1])
data = file.read().rstrip().split('\n')
for string in data:
    test = False
    for ign in ignore:
        if ign in string:
            test = True
            break
    if not string.startswith('!') and not test:
        print(string)

