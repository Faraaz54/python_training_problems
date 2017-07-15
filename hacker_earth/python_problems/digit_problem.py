inp = raw_input()
inp1, inp2 = inp.split()
num = [int(i) for i in inp1]
mov = int(inp2)

for key in range(len(num)):
    #print num[key]
    if mov > 0:
        if num[key] < 9:
            num[key] = 9
            mov -= 1
print ''.join(str(i) for i in num)

