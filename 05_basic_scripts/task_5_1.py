# -*- coding: utf-8 -*-
#!/usr/bin/env python3
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

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
IP = [int(datalist[i]) for i in range(4)]
print("Network:")
print("{oct[0]:<10}{oct[1]:<10}{oct[2]:<10}{oct[3]:<10}".format(oct = IP))
print("{oct[0]:08b}  {oct[1]:08b}  {oct[2]:08b}  {oct[3]:08b}  ".format(oct = IP))
print()
print('Mask:')
print('/{}'.format(datalist[-1]))
mask_str = '1' * mask + '0' * ( 32 - mask )
#print(mask_str)
mask_list = [ int(mask_str[0:8], 2), int(mask_str[8:16], 2), int(mask_str[16:24], 2), int(mask_str[24:], 2) ]
#print(mask_list)
print("{oct[0]:<10}{oct[1]:<10}{oct[2]:<10}{oct[3]:<10}".format(oct = mask_list))
print("{oct[0]:08b}  {oct[1]:08b}  {oct[2]:08b}  {oct[3]:08b}  ".format(oct = mask_list))
