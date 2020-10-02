import os

g = open('data', 'rt')
f = open("data.txt", "r")

for x in f:
	print(x)

	
print('Entire file: \n', g.read())
print(g.readlines())


print(os.system("pwd"))


