# Строки
# Объявление
friend = 'Максим Александрович \n Попов'
print(friend)

# Индексы - начинаяются с 0
friend = 'Максим Александрович Попов'
print(friend[2])

hello = 'hello world'
print(hello[3:8])

# Функции и методы строки
# 1. Функции
friend = 'Максим Александрович Попов'
print(len(friend))

# 2. Метод
friend_upper = friend.upper()
print(friend_upper)

# 3. На вхождение
friend = 'Максим Александрович Попов'
letters = 'андр'
print(letters in friend)

# Методы строк
friend = 'Максим Александрович Попов'
# Надо заменить фамилию на Иванов

friend_Ivanov = friend[:-5] +'Иванов'

print(friend_Ivanov)

# Метод для замены подстроки строкой
new_friend= friend.replace('Попов', 'Иванов')
print(new_friend)

#help(str)
print(dir(str))

# Популярные методы
print(friend.upper())
print(friend.lower())
print(friend.title())
print(friend.isdigit())

goods = 'Стол;;;стул;;;диван'
print(friend.split(';;;'))

# Форматирование строк
age = 20
name = 'Макс'

info = 'Имя: '+ name + 'age ' + str(age)
print(info)

# 2. метод формат
info = 'Имя: {} age: {}'.format(name,age)
print(info)

# 3. f
info =f'Имя: {name} age: {age}'
print(info)

# Неизменяемосто строк (изменяемые и неизменяемые типы)
friend = 'Максим александрович Попов'
upper_friend= friend.upper()
print(upper_friend)
friend = friend.upper()
print(friend)


l =[]
l.append(1)
print(l)

