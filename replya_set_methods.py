office = {'max','kate','john','leo','leo'}
print(type(office))

office.add('leo')
print(office)
office = ['max','kate','john','leo','leo']
print(set(office))

office = {'max','kate','john','leo'}
freelance= {'max','kate','pol'}

print((office-freelance))
print(freelance- office)
print(office&freelance)
print(office|freelance)