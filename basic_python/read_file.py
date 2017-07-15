'''readme = open('newtext', 'r').readlines()

print(readme)'''

readme = open('input.txt','r')
readme.seek(1)
readme.readlines()
count = 0
for word in readme:
    count += 1
    print word
    if count == 10:
        readme.close()
        break



