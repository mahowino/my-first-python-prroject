#persistently request the value of filename from the user until a value is given

usernames=['Tony','smith','Angela']

userchoice=''

while userchoice not in usernames:
    userchoice=input("Type in your username")

print("Hi "+userchoice)




