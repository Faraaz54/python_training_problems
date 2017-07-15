n = int(raw_input())
if n == 0:
    answer = 0
    print answer
if n >= 1 or n <= 1000:
    s = raw_input()    #[:(2 * n) - 1:1]
    if n == 1:
        answer = s
        print answer
    else:
        s_list = s.split(' ')
        print s_list
        prod = (10**9 + 7)
        answer = 1
        for i in s_list:
            answer = (answer * int(i)) % prod
        print answer


'''no_of_integer = raw_input()
integers = raw_input().split()
answer = 1
for value in integers:
    value_int = int(value)
    answer=(answer*value_int)%(10**9+7)
print(answer)'''

