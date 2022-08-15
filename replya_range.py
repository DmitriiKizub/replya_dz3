result = range(1,100)

print(result)
print(list(result))
result = range(4,56,2)
print(list(result))

# Сколько то раз
for i in range(100):
    print(i)

# индексация списка
quest = ['a','b','c','d']
for i in range(len(quest)):
    print(i)

for i,q in enumerate(quest):
    print(i)
    print(q)
    