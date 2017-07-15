def distance(x, y, x1, y1):
    if x == x1:
        return abs(y - y1)
    elif abs(x - x1) < abs(y - y1):
        return abs(y-y1)
    return abs(x-x1)


size = int(raw_input())
RI = lambda: map(int, raw_input().split())
lst = RI()
x1 = lst[0]
y1 = lst[1]
power = lst[2]
board = [[0 for i in range(size)] for j in range(size)]
board[x1][y1] = power

for x2 in range(size):
    for y2 in range(size):
        if (x2, y2) != (x1, y1):
            dist = distance(x2, y2, x1, y1)
            if dist > power:
                board[x2][y2] = 0
            else:
                board[x2][y2] = abs(dist - power)




for row in board:
    print '{0}'.format(' '.join(map(str,row)))


'''a=input()
l=[int(x) for x in raw_input().split()]
for i in range(a):
    for j in range(a):
        if(abs(l[0]-i)>abs(l[1]-j)):
            print max(0,l[2]-abs(l[0]-i)),
        else:
            print max(0,l[2]-abs(l[1]-j)),
    print '''

