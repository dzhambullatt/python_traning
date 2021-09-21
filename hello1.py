from datetime import datetime
# person = {'name': 'ivan', 'surname': 'rizvan'}

# d = dict(name='petr', ihvan='amhad')


# new = {'name': 'dima', 'amhad': 'budulay'}
# person.update(new)

# print(person)

# i = 0
# while i <= 9:
# 	i += 1
# 	print(i)


# i = 1 
# while i <= 5:
# 	print(i)
# 	i += 1 


# x = int(input())
# while x > 0:
#     y = x
#     while y > 0:
#         y -= 1
#         print(y)
#     x -= 1
# print('stop')



# import random

# a = ['dffdf', 'ffdfd', 'eeee', 'ffff']

# print(random.choice(a))


#strok = ['ddddd_ZZZZ', 'aaaaa_sssss', 'zzzzz_qqqqq', 'fffff_aaa']

# for l in i:
# 	print(l)

# 	

# for i in strok:
# 	nn = i.split('_')[0].title()
# 	print(nn)

# person = {'name': 'ivan', 'surname': 'pupkin'}

# d = dict(name='petr', tel='12345')

# print(d)

# name = person['name']
# print(name)

# tel = d.get('tel', '12344444')
# print(tel)


# for i in person:
# 	print(i)


# for i in person.keys():
# 	print(i)

# for i in person.items():
# 	print(i)

# for key, value in person.items():
# 	print(key, value)


# inter = 0
# while inter <= 100:
# 	print(inter)
# 	inter += 1

# jack = {
# 	'name': 'jack',
# 	'car': 'bmw'
# }

# jhon = {
# 	'name': 'jhon',
# 	'car': 'audi'
# }

# users = [jack, jhon]

# cars = [i.get('car') for i in users]

# print(cars)


# name = ['jack', 'jhon', 'oleg', 'ula']

# #new_names = [n for n in name if n.startswith('j')]

# #print(new_names)

# new_name = []
# for n in name:
# 	if n.startswith('j'):
# 		new_name.append(n)

# print(new_name)

def timeit(func):
	def wrapper():
		start = datetime.now()
		result = func()
		print(datetime.now() - start)
		return result
	return wrapper

@timeit
def one():
	#start = datetime.now()
	l = []
	for i in range(10**4):
		if i % 2 == 0:
			l.append(i)
	#rint(datetime.now() - start)
	return l

@timeit
def two():
	#start = datetime.now()
	l = [x for x in range(10**4) if x % 2 == 0]
	#print(datetime.now() - start)
	return l




l1 = one()
l2 = two()

# print(l1)
# print(l2)