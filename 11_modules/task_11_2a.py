#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
import draw_network_graph
from task_11_1 import parse_cdp_neighbors
topolist = {}
temp = {}
conflist = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']

for i in conflist:
    with open(i) as file:
        temp = file.read()
    current = parse_cdp_neighbors(temp)
    for j in current.keys():
        if topolist.get(current[j]) != j or topolist.get(current[j]) == 'None':
            topolist.update({(j): (current[j]) })
print(topolist)
draw_network_graph.draw_topology(topolist, output_filename='test2a')
