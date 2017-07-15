#You are given an integer N. You need to print the series of all prime numbers till N.

''' s = 9


def perfect_square(i):
    p_square = 0
    for i in range(2, i):
        i_squared = i**i
        if i_squared <= i:
            p_square = i
    return p_square
'''


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

'''start = raw_input()
end = raw_input()
print find_primes(int(start), int(end))'''

'''t = int(raw_input())
lst = []
for num in range(2,t+1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           lst.append(num)
str = ' '.join(str(a) for a in lst)
print str   '''





















