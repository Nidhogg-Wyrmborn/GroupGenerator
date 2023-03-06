import pickle

with open("test.txt", 'rb') as f:
    a = pickle.load(f)

a.main()
