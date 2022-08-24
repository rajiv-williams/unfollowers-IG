import os

files = ['followers.txt','following.txt']

for file in files:
    if(os.path.isfile(file)):
        os.remove(file)