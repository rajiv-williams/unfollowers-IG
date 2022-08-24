from distutils.log import error
import instaloader
import itertools
import threading
import time
import sys
import os

#userDetails file
filename = "userDetails.txt"

#Took 1min 36s to load all my followers and following (931 vs 550)
loadingDone = False
errorOccurred = False

def animate():
    for frame in itertools.cycle(['0oo','o0o','oo0']):
        if loadingDone:
            break
        sys.stdout.write('\rLoading followers ' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
    if errorOccurred:
        sys.stdout.write('\rERROR: Failed to load followers\n')
    else:
        sys.stdout.write('\rSuccessfully loaded followers!\n')

#remove userDetails file for security reasons
def removeUserDetails():
    if(os.path.isfile(filename)):
        os.remove(filename)

# #loading follower info ---
file = open(filename,"r")
userDetails = file.read().split("\n")
file.close()
removeUserDetails()   
myUsername = userDetails[0].split(":")[1]
password = userDetails[1].split(":")[1]
L = instaloader.Instaloader()
L.login(myUsername,password)

#threading for loading
thread = threading.Thread(target=animate)
thread.start()

 

profile = instaloader.Profile.from_username(L.context,myUsername)

# following = profile.get_followees()
# followers = profile.get_followers()

followingList = []
followerList = []
followerCount = 0
for user in profile.get_followers():
    followerList.append(user.username)
    file = open("followers.txt", "a+")
    file.write(followerList[followerCount])
    file.write("\n")
    file.close()
    # print(followerList[count])
    followerCount = followerCount + 1

followingCount = 0
for user in profile.get_followees():
    followingList.append(user.username)
    file = open("following.txt", "a+")
    file.write(followingList[followingCount])
    file.write("\n")
    file.close()
    # print(followingList[count])
    followingCount = followingCount + 1

time.sleep(2)
loadingDone = True

print("\nUser: "+ myUsername+ "\nFollowers: " + followerCount + "\nFollowing: " + followingCount + "\n")