import pickle
import os
def get_pkl(file):
    with open(file, 'rb') as fr:
        data = pickle.load(fr)
        # print(type(data))
        # print(len(data))
        return data

data = get_pkl('./data/test/5_core/user_reviews.pkl')
# print(data)
# print(data)
# print(len(data))
print(data[0])
# print(len(data[0][1]))
# print(len(data[0]))
print(len(data[0]))
# print(data[1])
# print(len(data[1][1]))
# print(data[2000])
# print(len(data[2000]))