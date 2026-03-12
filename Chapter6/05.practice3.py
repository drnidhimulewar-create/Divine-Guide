#a spam comment is defined as a text containing following keywords:
# "Make a lot of money" , "buy now","subscribe this", "click this". Write a program tomdetect these spams.
p1="Make a lot of money"
p2=" buy now"
p3="subscribe this"
p4="click this link"
p5="quick money"

message = input("Ente your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")
