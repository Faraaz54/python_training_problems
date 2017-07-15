intermediate_list = []
for i in range(1, 109, 3):
    if i%2 == 0:
        d3 = {i: 'AS', i+1: 'MS', i+2: 'WS'}
    else:
        d3 = {i:'WS', i+1: 'MS', i+2:'AS'}

    intermediate_list.append(d3)

seating_arrangement = dict(enumerate(intermediate_list, start=1))

'''pair of set of seats facing each other'''
set_pair = []

for i in range(1, 37, 4):
    set_pair.append((i, i+3))
    set_pair.append((i+1, i+2))

seat_set_no = 0
seat_type = ''
facing_set_no = 0
facing_seat_no = 0
solution = []


inp = int(raw_input())
for _ in xrange(0, inp):
    s = int(raw_input())
    for set_no in seating_arrangement:
        for seat_no in seating_arrangement[set_no]:
            if seat_no == s:
                seat_type = seating_arrangement[set_no][seat_no]
                seat_set_no = set_no

    for set1, set2 in set_pair:
        if seat_set_no == set1:
            facing_set_no = set2
        elif seat_set_no == set2:
            facing_set_no = set1

    for seat in seating_arrangement[facing_set_no]:
        if seating_arrangement[facing_set_no][seat] == seat_type:
            facing_seat_no = seat

    solution.append((facing_seat_no, seat_type))

for sn, st in solution:
    print sn, st

'''for _ in xrange(int(raw_input())):
    s=int(raw_input())
    n=s%12
    if n==1:
        print str(s+11)+" WS"
    elif n==2:
        print str(s+9)+" MS"
    elif n==3:
        print str(s+7)+" AS"
    elif n==4:
        print str(s+5)+" AS"
    elif n==5:
        print str(s+3)+" MS"
    elif n==6:
        print str(s+1)+" WS"
    elif n==7:
        print str(s-1)+" WS"
    elif n==8:
        print str(s-3)+" MS"
    elif n==9:
        print str(s-5)+" AS"
    elif n==10:
        print str(s-7)+" AS"
    elif n==11:
        print str(s-9)+" MS"
    else:
        print str(s-11)+" WS"'''

