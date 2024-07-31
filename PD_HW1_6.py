my_dict = {'Vadim': 1993, 'Sasha': 2001, 'Igor': 1997}
print('Dict:', my_dict)
print('Existing value:', my_dict['Vadim'])
print('Not existing value:', my_dict.get('Vlad'))
my_dict.update({'Viktor': 1998, 'Alexandra': 2000})
print('Deleted value:', my_dict.pop('Igor'))
print('Modified dictionary:', my_dict)
print()

my_set = {'Vadim', 1993, 1742, True, 222, 'Vlad', 1993, 222}
print('Set:', my_set)
my_set.update('V', (1321,133))
my_set.remove(222)
print('Modified set:', my_set)
