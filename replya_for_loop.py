

# dict
friendss = {
        'name': 'max',
        'age': 20,
        'has_car': True
}
for key in friendss:
    print(key)
    print(friendss[key])

# Только значния
for v in friendss.values():
    print(v)

# По парам ключ значения
for key,val in  friendss.items():
    print(key)
    print(val)

name, age, has_car = ('max', 23, True)
print(name, age, has_car)