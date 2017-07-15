import os

names = ['gary', 'hazard', 'torres']


for name in names:
    print'hello there,', name

print(', '.join(names))

who = 'gary'

number = '15'

print who, 'ate', number, 'apples'
print('{0} ate {1} apples'.format(who, number))


location = 'C:\\Users\\farazz\\python_training'
file_name = 'example.txt'

file_location = location+ '\\' + file_name
print file_location
print('\\'.join([location, file_name]))

#file_open = open('file_location', 'r')

#while True:
   # line = file_open.readline()
    #print line
    #if not line:
        #break

with open(os.path.join(location, file_name)) as f:
    print f.readline()










