l = [i for i in raw_input()]
s = l[0]
count = 0
message = 'Good luck!'
for i in range(0, len(l)):
    if l[i] == s:
        count += 1
        if count == 6:
            message = 'Sorry, sorry!'
            break
    else:
        s = l[i]
        count = 1

print message








