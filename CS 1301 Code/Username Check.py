username=input("Please enter a username you wish to check: ")

def is_valid_username(username):
    status_checker=True
    if len(username) < 6:
        status_checker=False
    if len(username) > 12:
        status_checker=False

    if status_checker==True:
        print("True")
    else:
        print("False")

is_valid_username(username)
reattempt=input("Would you like to check another username (y/n): ")
while reattempt=="y":
    username=input("Please enter a username you wish to check: ")
    is_valid_username(username)
    reattempt=input("Would you like to check another username (y/n): ")
else:
    print("Exiting program")
    exit