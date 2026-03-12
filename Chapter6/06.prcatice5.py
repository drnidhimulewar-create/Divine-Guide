#Write a program which finds out whether given name is present in a list or not.
l = ["radha","mohan", "shiv","gauri"]

name = input("Enter your name:")

if(name in l):     # 'in' keyword iis imp
    print("Your name is in the list.")
else: 
    print("Your name is not in the list.")   