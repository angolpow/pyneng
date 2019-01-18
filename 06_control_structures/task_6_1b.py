# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

TRY = False

while not TRY:
	try:
		IP = input('Enter IP address: ')
		count = 0
		IPSTR = IP.split('.')
		FOCT = int(IPSTR[0])
	
		for i in IPSTR:
			if int(i) / 255 > 1:
				int('a')
			count += 1
		
		if count != 4:
			int('a')
		TRY = True
	except:
		TRY = False
		print('Incorrect IPv4 address')

if IP == '255.255.255.255':
	print("local broadcast")
elif IP == '0.0.0.0':
	print('unassigned')
elif FOCT > 0 and FOCT < 224:
	print('unicast')
elif FOCT > 223 and FOCT < 240:
	print('multicast')
else:
	print('unused')
