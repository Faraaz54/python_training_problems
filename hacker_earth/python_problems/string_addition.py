


sol = []
for _ in xrange(0, int(raw_input())):
    s = raw_input()
    #w = [i for i in s]
    #print w

    #t = [s[len(s) - 1 - count] for count in xrange(len(s))]
    #print t

    T = []
    st = 0
    for i in xrange(0, len(s)):
        v = (ord(s[i]) + ord(s[len(s) - 1 - i])) - 96
        if v <= 122:
            st = chr(v)
        elif v > 122:
            v = v - 26
            st = chr(v)

        '''k = v % 218
        a = 97
        if k == 194 or k == 2:
            st = chr(a+1)
        elif k == 195 or k == 3:  
            st = chr(a+2)
        elif k == 196 or k == 4:
            st = chr(a+3)
        elif k == 197 or k == 5:
            st = chr(a+4)
        elif k == 198 or k == 6:
            st = chr(a+5)
        elif k == 199 or k == 7:
            st = chr(a+6)
        elif k == 200 or k == 8:
            st = chr(a+7)
        elif k == 201 or k == 9:
            st = chr(a+8)
        elif k == 202 or k == 10:
            st = chr(a+9)
        elif k == 203 or k == 11:
            st = chr(a+10)
        elif k == 204 or k == 12:
            st = chr(a+11)
        elif k == 205 or k == 13:
            st = chr(a+12)
        elif k == 206 or k == 14:
            st = chr(a+13)
        elif k == 207 or k == 15:
            st = chr(a+14)
        elif k == 208 or k == 16:
            st = chr(a+15)
        elif k == 209 or k == 17:
            st = chr(a+16)
        elif k == 210 or k == 18:
            st = chr(a+17)
        elif k == 211 or k == 19:
            st = chr(a+18)
        elif k == 212 or k == 20:
            st = chr(a+19)
        elif k == 213 or k == 21:
            st = chr(a+20)
        elif k == 214 or k == 22:
            st = chr(a+21)
        elif k == 215 or k == 23:
            st = chr(a+22)
        elif k == 216 or k == 24:
            st = chr(a+23)
        elif k == 217 or k == 25:
            st = chr(a+24)
        elif k == 0 or k == 26:
            st = chr(a+25)
        else:
            st = chr(a)'''

        T.append(st)
    sol.append(''.join(T))

for i in sol:
    print i
