L = raw_input()
L_tuple = (int(L), int(L))
N = raw_input()
#n = int(N)
s = []
for i in range(int(N)):
    l, r = raw_input().split()
    s.append((int(l), int(r)))

for i in s:
    if i[0] < L_tuple[0] or i[1] < L_tuple[1]:
        print 'UPLOAD ANOTHER'
    elif i[0] >= L_tuple[0] or i[1] >= L_tuple:
        if i[0] == i[1]:
            print 'ACCEPTED'
        else:
            print 'CROP IT'


'''640
10
320 320
640 640
640 320
320 640
640 480
500 1000
1000 500
500 500
1000 1000
1 1'''




