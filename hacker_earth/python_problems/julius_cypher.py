def get_cipher(cipher_string):
    prod = 1
    for i in cipher_string:
        prod *= (ord(i) % 97)+1
    return prod


for _ in xrange(int(raw_input())):
    s = list(raw_input())
    if s == list(reversed(s)):
        print 'Palindrome'
    else:
        print get_cipher(s)