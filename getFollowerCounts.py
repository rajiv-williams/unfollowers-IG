import instaloader
import itertools
import threading
import time
import sys
import os

#Took 1min 36s to load all my followers and following (931 vs 550)
loadingDone = False

def animate():
    for frame in itertools.cycle(['0oo','o0o','oo0']):
        if loadingDone:
            break
        sys.stdout.write('\rLoading followers ' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rSuccessfully loaded followers!\n')



# #loading follower info ---
filename = "userDetails.txt"
file = open(filename,"r")
userDetails = file.read().split("\n")
myUsername = userDetails[0].split(":")[1]
password = userDetails[1].split(":")[1]
file.close()
L = instaloader.Instaloader()
L.login(myUsername,password)

#threading for loading
thread = threading.Thread(target=animate)
thread.start()

#remove userDetails file for security reasons
if(os.path.isfile(filename)):
    os.remove(filename)

profile = instaloader.Profile.from_username(L.context,myUsername)

# following = profile.get_followees()
# followers = profile.get_followers()

followingList = []
followerList = []
count = 0
for user in profile.get_followers():
    followerList.append(user.username)
    file = open("followers.txt", "a+")
    file.write(followerList[count])
    file.write("\n")
    file.close()
    # print(followerList[count])
    count = count + 1

count = 0
for user in profile.get_followees():
    followingList.append(user.username)
    file = open("following.txt", "a+")
    file.write(followingList[count])
    file.write("\n")
    file.close()
    # print(followingList[count])
    count = count + 1

time.sleep(2)
loadingDone = True