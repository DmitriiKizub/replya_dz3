# Словари
name = 'max'
age = 20
has_car = True

friend = (name,age, has_car)

friend = {
    'name': name,
    'age': 20,
    'has_car': True
    }
print(type(friend))

# Индексы? у словаря есть ключи и мы можем их использовать
print(friend['age'])
print(friend['has_car'])

# Функции
print(len(friend))

# Оператор вхождения
# Проверить по ключам
print('name' in friend)

# Методы (действия). Добавить, удалить, изменить
# Добавить, изменить
print(friend)
friend['has_wife'] = True
print(friend)

# Удалить
del friend['has_wife']
print(friend)

# Методы, получить значение
#  Ключи
print(list(friend.keys()))
# Значения
print(list(friend.values()))
# пары ключ значение - кортеж
print(list(friend.items()))

print('max' in friend.values())
