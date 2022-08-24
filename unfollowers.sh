echo Starting Unfollowers program...
python ./removeFiles.py

#Ask user for username and password
javac UserInput.java
java UserInput

#Get followers and show loading screen (Takes a long time, cuz if there were 1M followers, would take forever
python ./getFollowerCounts.py

javac WhoUnfollowedMe.java
java WhoUnfollowedMe