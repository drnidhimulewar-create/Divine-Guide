#Wite wheter given number is prime or not.
n = int(input("Enter a numeber:"))

for i in range(1,n):
    if(n%i) == 0:
        print("Number is prime")
        break
    else:

        print("Number is not prime.")    