import pickle

dict_1 = {1 : 'F', 2 : 'T', 3 : 'U'}

pickle_out = open('dict.pickle', 'wb')

pickle.dump(dict_1, pickle_out)

pickle_out.close()

pickle_in = open('dict.pickle', 'rb')

dict_2 = pickle.load(pickle_in)

print dict_2
print dict_2[1]









