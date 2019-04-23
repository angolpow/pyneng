#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def config_to_list(fname):
    ''''''
    with open(fname) as file:
        result = {}
        dic23 = {}
        for line in file:
            if not check_ignore(line,ignore) and not line.startswith('!'):
                if not line.startswith(' '):
                    commandl1 = line.strip()
                    result[commandl1] = {}
                elif not line.startswith('  '):
                    commandl2 = line.strip()                
                    result[commandl1][commandl2] = []
                else:
                    commandl3 = line.strip()
                    result[commandl1][commandl2].append(commandl3)
                    
        for key in result.keys():
            if result[key] == {}:
                result[key] = []
    return(result)

print(config_to_list('config_r1.txt'))

