#Practice set python chapter 5

#PRG1
#Write a program to create a dictonary of Hindi words with values as their english translation. Provide user with an option to look it up.
words = {
         "madad" :"Help",
         "kangi" :"comb",
         "mej":"table",
}

word = input("Enter the word you want the meaning of:")
print(words[word])

#PRG2
#Write a program to input eight numbers from the user and display all the unique numbers(once).
s = set()
n = input("Enter number :")
s.add(int(n))
n = input("Enter number :")
s.add(int(n))
n = input("Enter number :")
s.add(int(n))
n = input("Enter number :")
s.add(int(n))
n = input("Enter number :")
s.add(int(n))
n = input("Enter number :")
s.add(int(n))
n = input("Enter number :")
s.add(int(n))
print(s)

#PRG3
#Can we have  18 an integer and a string as well.
s = set()
s.add(18)
s.add("18")

print(s)

#PRG4
#***What will be the length of this set
'''s=set()
   s.add(20)
   s.add(20.0)
   s.add('20')''' #the length of s after these operations?  
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))

#PROG5
'''
Que: s={}
     what is the type of 's'?'''
#ans~~~~DICTONARY~~~~~

#PRG6
#Create an empty dictonary. Allow 4 friends to enter their favourite language as valus and use keys as their names. Assume their names are unique.


print(d)
#PRG7 answer of code if NAME(key) of the two friends is same
'''
Enter friend's name:ram
Enter the languge name:c
Enter friend's name:sita
Enter the languge name:c++
Enter friend's name:lakshman
Enter the languge name:java
Enter friend's name:lakshman
Enter the languge name:python
{'ram': 'c', 'sita': 'c++', 'lakshman': 'python'}'''

#PRG8 answer of the code if LANGUAGE(value) of the two friends is same
'''
{'shree krishna': 'c', 'shree radha': 'c',
 'shree ram': 'c++', 'maa sita': 'c++'}'''

#PRG9
#Can you change the value inside a list which is contained in set S?
S= {8,7,12,"Harry",[1,2]}
#ans No,you cannot do it since the set is immutable and hashable. Lists are mutable and not hashable,so theycant be added to set.
# To achieve similar functionality , use tuple to list , since tulpe is immutable and hashable.
