#!/bin/bash

#file destination for username and password
userDetails=./userDetails.txt

echo Starting Unfollowers program...
python ./removeFiles.py

echo "Enter Username: "

# read username and echo username in terminal
read username

echo "Enter Password: "

# -s is silent mode
read -s password

#-e allows \n characters
echo -e "Username:$username\nPassword:$password"> $userDetails

#Get followers and show loading screen (Takes a long time, cuz if there were 1M followers, would take forever
python ./getFollowerCounts.py

javac WhoUnfollowedMe.java
java WhoUnfollowedMe