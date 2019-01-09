# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
PARAM_LIST = ["Protocol:", "Prefix:", "AD/Metric:", "Next-Hop:", "Last update:", "Outbound Interface:"]
DATA = ospf_route.replace(",", " ").replace("[", " ").replace("]", " ").replace("via", " ").replace("O", "OSPF").split()
for i in range(6): print("{0:24}{1:24}".format(PARAM_LIST[i],DATA[i]))
