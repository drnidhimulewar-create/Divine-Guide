subject1= int(input("Enter marks1="))
subject2= int(input("Enter marks1="))
subject3= int(input("Enter marks1="))

total_percentage = ((subject1+subject2+subject3)/300)*100

if(total_percentage >=40):
    print("Passed.")
else:
    print("Failed.")