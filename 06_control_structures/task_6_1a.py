# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = input('Enter IP address: ')
TRY = "true"
count = 0

try:
	IPSTR = IP.split('.')
	FOCT = int(IPSTR[0])
	
	for i in IPSTR:
		if int(i) / 255 > 1:
			TRY = "false"
		count += 1

except:
	TRY = "false"

if TRY == "true" and count == 4 :
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
else:
	print('Incorrect IPv4 address')

