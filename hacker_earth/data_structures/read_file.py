readme = open('input.txt','r')
count = 0
savefile = open('output.txt','w')
for word in readme.readlines():
    count += 1
    text = '{0}'.format(word)
    savefile.write(text)
    if count == 10:
        readme.close()
        savefile.close()
        break

