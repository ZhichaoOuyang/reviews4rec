import pickle
import os
def get_pkl(file):
    with open(file, 'rb') as fr:
        data = pickle.load(fr)
        # print(type(data))
        # print(len(data))
        print(len(data[0][0]))
        print(len(data[0][1]))

get_pkl('./data/clothing/5_core/user_reviews.pkl')