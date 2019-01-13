# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

MODE = input('Enter interface mode (access/trunk): ')
IF = input('Enter interface type and number: ')
param_list = {'access': 'Enter VLAN number:', 'trunk': 'Enter allowed VLANs:'}
VLAN = input('{} '.format(param_list[MODE]))

access = '\n'.join(access_template)
trunk = '\n'.join(trunk_template)
param_list = {'access': access, 'trunk': trunk}

print('interface {}'.format(IF))
print('{}'.format(param_list[MODE]).format(VLAN))
