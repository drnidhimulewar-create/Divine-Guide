#Write a program to find whether a giaven username contains less than 10 characters or not.
username = input("Enter a username:")

if(len(username)<10):
    print("Your username conatins less than 10 characters. You're good to go!")
else:
    print("Your username exceeds limit more than 10 characters.")    