# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

param_list = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']
file = open('ospf.txt')

for line in file:
	list = line.replace(',', ' ').replace("[", " ").replace("]", " ").replace("via", " ").replace('O', 'OSPF').split()
	for i in range(len(param_list)):
		print('{:23}{:23}'.format(param_list[i], list[i]))
	print()
