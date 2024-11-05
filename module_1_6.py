#Словарь
my_dict = {'Anton':1998, 'Anna':2005, 'kirill':2001,'Masha':1999}
print(my_dict)

print('Значение по существующему ключу: ', my_dict.get('Anna'))
print('Значение по отсутствующему ключу: ', my_dict.get('Ivan'))

my_dict.update({'Kristina':1998 , 'Sasha':2003})
print(my_dict)

print('Удалённое значение: ', my_dict.pop('Anton'))
print(my_dict)

#Множество
my_set = {1.25  , 2, 3, 3, 'Cat', 2,'Cat'}
print(my_set)
my_set.add(5)
my_set.add('Black cat')
print(my_set)
my_set.remove(2)
print(my_set)