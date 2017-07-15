'''You are given a string S. Count the number of occurrences of all the digits in the string S.'''
'''CFTPM6547J'''

'''\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.
Modifiers:

{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code
White Space Charts:

\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return
Characters to REMEMBER TO ESCAPE IF USED!

. + * ? [ ] $ ^ ( ) { } | \''''

import re
s = raw_input()
num1 = []
num = [i for i in re.findall('\d+|\D+', s) if i.isdigit()]
for word in num:
    for i in word:
        num1.append(int(i))

num_dict = {}
for i in range(10):
    num_dict.update({i:0})

for dig in num1:
    for key in num_dict:
        if dig == key:
            num_dict[key] += 1

for key in num_dict:
    print key, num_dict[key]

















