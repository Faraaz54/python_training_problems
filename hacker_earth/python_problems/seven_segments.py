def energy_consumption(num):
    sum1 = 0
    consumption_list = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}
    num_1 = [j for j in num]
    for i in range(len(num_1)):
        sum1 += consumption_list[num_1[i]]
    return sum1

for _ in xrange(int(raw_input())):
    final_list = []
    inp = int(raw_input())
    l = [(energy_consumption(i), i) for i in raw_input().split()]
    l.sort(key=lambda x: x[0])
    #print l
    r, k = l[0]
    print k























