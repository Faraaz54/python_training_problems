def uses_all(word , s):
    j = 0
    for i in s:
        if i in word:
            j = j + 1
    if j == len(s):
        return word



fin = open('words.txt', 'r')
s = 'aeiou'
count = 0
while True:
    line = fin.readline()
    word = line.strip()
    match_word = uses_all(word, s)
    if match_word != None:
        count += 1
        print match_word
    if not line:
        break

print count


fin.close()
