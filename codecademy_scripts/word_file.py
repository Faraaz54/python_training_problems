fin = open('words.txt', 'r')
total = 0
count = 0
while True:
    line = fin.readline()
    total = total + 1
    word = line.strip()
    if 'e' not in word:
        count = count + 1
    if not line:
        break

print count
print total
percentage = float(count) / total * 100.00
print percentage


fin.close()
