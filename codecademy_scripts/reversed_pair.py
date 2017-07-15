def check_reversed(word, let, length):
    for i in range(0, len(word_list) - 1):
        buff = word_list[i]
        if buff[0] == let:
            if len(buff) == len(word):
                if buff == word:
                    return True









			
			
fin = open('words.txt', 'r')
word_list = []
while True:
    line = fin.readline()
    word = line.strip()
    word_list.append(word)
    if not line:
        break
		
match_list = []

for i in range(0, len(word_list) - 1):
    buff = word_list[i]
    rev = buff[::-1]
    le = rev[0]
    l = len(buff)
    if check_reversed(rev, le, l):
        print buff, rev
	    #match_list.append((buff, rev))
		
print match_list
		
		

		
        
		




fin.close()
