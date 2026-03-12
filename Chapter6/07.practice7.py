#Write the program to fine out a given post is talking about "Shri Ram " or not.
post = input("Type the post:")



if("Ram".lower() in post.lower()):
    print("This post is talking about Shri Ram.")
else:
    print("This pot is not talking about Shri Ram.")