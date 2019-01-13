#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

rawdata = argv[-1]
print(rawdata)
datalist = rawdata.replace('.', ' ').replace('/', ' ').split()
mask = int(datalist[-1])
ip_list = [ int(datalist[i]) for i in range(4) ]
ip_str = '{oct[0]:08b}{oct[1]:08b}{oct[2]:08b}{oct[3]:08b}'.format(oct = ip_list)

net_str = ip_str[:mask] + "0" * ( 32 - mask )
net_list = [ int(net_str[0:8], 2), int(net_str[8:16], 2), int(net_str[16:24], 2), int(net_str[24:], 2) ]

mask_str = '1' * mask + '0' * ( 32 - mask )
mask_list = [ int(mask_str[0:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), int(mask_str[24:], 2) ]

print()
print('Network:')
print("{oct[0]:<10}{oct[1]:<10}{oct[2]:<10}{oct[3]:<10}".format(oct = net_list))
print("{oct[0]:08b}  {oct[1]:08b}  {oct[2]:08b}  {oct[3]:08b}  ".format(oct = net_list))

print()
print('Mask:')
print('/{}'.format(mask))
print("{oct[0]:<10}{oct[1]:<10}{oct[2]:<10}{oct[3]:<10}".format(oct = mask_list))
print("{oct[0]:08b}  {oct[1]:08b}  {oct[2]:08b}  {oct[3]:08b}  ".format(oct = mask_list))
