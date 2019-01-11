# -*- coding: utf-8 -*-
'''
Задание 5.1a

Всё, как в задании 5.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 5.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

rawdata = input()
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
