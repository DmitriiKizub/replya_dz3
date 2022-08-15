# Объявление
friends = []
friends = [1, True, 'max', 1.2]
friends = ['max','kate','john','leo']

# индексы
print(friends[1])
print(friends[1:3])

# Функции
# Длина
print(len(friends))

# Оператор вхождения
print('max' in friends)
print('poll' in friends)

# Основные методы (действия)
# Добавление, изменение, удаление
# Добавление
friends.append('poll')
print(friends)

# Изменения
friends.insert(2, 'maria')
print(friends)

# Удаление
# 1. через remove
friends.remove('maria')
print(friends)
# 2. изменения
friends[3]= 'leonid'
print(friends)
# 3. удаление по индексу
del friends[1]
print(friends)


# сортировка
friends.sort()
print(friends)