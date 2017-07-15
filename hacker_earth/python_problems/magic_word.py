def find_primes(start, end):
    primes = []
    if end == 1:
        print 1
    p_list = [x for x in range(2, end+1)]
    for num in p_list:

        for i in range(2, num):

            if num % i == 0:
                break
        else:
            if num >= start and num <= end:
                primes.append(num)
    return primes

def find_position(lst, key):
    # Find i such that A[i] <= key, in the sorted array A
    # Return -1 if key < A[0]
    low = 0
    high = len(lst) - 1
    while low <= high:
        if lst[low] > key:
            return low - 1
        elif lst[high] < key:
            return high

        mid = (low + high) / 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def all_primes():
    start = 65
    end = 122
    for nums in find_primes(start, end):
        yield nums


p_list = [i for i in all_primes()]

for _ in range(1, int(raw_input()) + 1):
    len_s = int(raw_input())
    s = raw_input()
    #lst = [ord(x) for x in s]
    T = [''] * len_s
    num = 0

    for j, c in enumerate(s):
        #print c , ord(c)
        i = find_position(p_list, ord(c))
        if i == -1 :
            i += 1
            num = chr(p_list[i])
        elif ord(c) > p_list[len(p_list) - 1]:
            num = chr(p_list[len(p_list) - 1])
        elif p_list[i] == ord(c):
            num = chr(p_list[i])
        elif p_list[i] != ord(c):
            if ord(c)-p_list[i] <= p_list[i+1]-ord(c):
                num = chr(p_list[i])
            else:
                num = chr(p_list[i+1])
        #print num, ord(num)
        T[j] = num
    print ''.join(T)



'''def findKeyPosition(A, key):
    # Find i such that A[i] <= key, in the sorted array A
    # Return -1 if key < A[0]
    low = 0
    high = len(A) - 1
    while low <= high:
        if A[low] > key:
            return low-1
        elif A[high] < key:
            return high
            
        mid = (low + high)/2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
 
 
P = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 
    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 
    173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257
]
 
for _ in xrange(input()):
    N = input()
    S = raw_input().strip()
    T = ['']*N
    for k, c in enumerate(S):
        i = findKeyPosition(P, ord(c))
        t = c
        if P[i] != ord(c) or P[i] < 65 or P[i] > 122:
            if P[i] < 65:
                t = chr(67)
            elif ord(c)-P[i] <= P[i+1]-ord(c) or P[i+1] > 122:
                t = chr(P[i])
            else:
                t = chr(P[i+1])
        T[k] = t
    print ''.join(T)'''




