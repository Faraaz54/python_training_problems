sample_string = raw_input()

s_dict = dict(enumerate(sample_string))

for key in s_dict:
    if s_dict[key].islower():
        to_upper = s_dict[key].upper()
        s_dict.update({key: to_upper})
    elif s_dict[key].isupper():
        to_lower = s_dict[key].lower()
        s_dict.update({key: to_lower})


s_list = [s_dict[key] for key in s_dict]

print ''.join(s_list)

'''S = raw_input()
text = []
text = list(S)

for x, key in enumerate(text):
    if key.isupper():
        text[x] = key.lower()
    else:
        text[x] = key.upper()

M = "".join(text)
print (M)'''



