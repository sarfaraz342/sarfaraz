import pickle
#fp=open("pickle1.txt","wb")
#CN=["dhoni","virat","dhawan"]
#pickle.dump(CN,fp)
#fp.close()##



with open("pickle1.txt", "rb") as fp:
    unpickled_data = pickle.load(fp)
    print(unpickled_data)



