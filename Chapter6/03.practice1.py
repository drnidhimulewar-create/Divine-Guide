#Write a program to find greatest among four numbers entered by the user.
a1= int(input("Enter anumber:"))
a2= int(input("Enter anumber:"))
a3= int(input("Enter anumber:"))
a4= int(input("Enter anumber:"))

if(a1>a2 and a1>a3 and a1>a4):
   print("First number is greatest.",a1)
elif(a2>a1 and a2>a3 and a2>a4):
   print("Second number is greatest.",a2)
elif(a3>a1 and a3>a2 and a3>a4):
   print("Third number is greatest.",a3)
else:
   print("Fourth number is greatest.",a4) 
