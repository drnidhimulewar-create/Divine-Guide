#Write a program to greet a person names stored in list 'L' and which starts with S.
#L=[" Hari","Shiv","Madhav","Shankar"]
l = ["Hari","Shiv","Madhav","Shankar" ]
for name in l:
    if(name.startswith("S")):
       print(f"Hello {name}")
