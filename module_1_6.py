my_dist = {'Oleg': 1961, 'Olga': 1967}
print(my_dist['Oleg'])
print(my_dist.get('Ivan', 'Такого ключа нет'))
my_dist.update({'Polina':2000,
                'Ksenia':1990})
print(my_dist)
print(my_dist.pop('Ksenia'))
print(my_dist)
my_set = {1, 2, 3.5, 4, 3, 2, 1, 'One', 'Two', 'One'}
print(my_set)
my_set.add(5)
my_set.add('Three')
print(my_set)
my_set.remove('Two')
print(my_set)