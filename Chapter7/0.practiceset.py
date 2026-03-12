#Write a program to print multiplication tablr of given number using loop.
n =int(input("Enter a number:"))

for i in range(1,11):
    print(f"{n}*{i}={n*i}")