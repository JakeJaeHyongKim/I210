#4.13 (Write your solutions as Boolean conditions - they should evaluate to True or False)
s="abcdefghijklmnopqrstuvwxyz"
#A
print (s[1:3]=="bc")
#B
print (s[:14]=="abcdefghijklmn")
#C
print (s[14:]=="opqrstuvwxyz")
#D
print (s[1:-1]=="bcdefghijklmnopqrstuvwxy")

#4.16 (By dictionary order, they mean alphabetical order)
first=input("Enter first word:")
second=input("Enter second word:")
third=input("Enter third word:")

words=[first, second, third]
if words==sorted(words):
    print(True)

#4.19
first="Marlena"
last="Sigel"
middle="Mae"
#A
print(last+",",first,middle)
#B
print(last+",",first,middle[0]+".")
#C
print(first,middle[0]+".",last)
#D
print(first[0],middle[0],last,sep=". ")
#E
print(last+",",middle[0]+".")
#I used (first,middle,last,sep="."), but it turned out w/o space that is shown in example.

#4.20
sender="tim@abc.com"
recipient="tom@xyz.org"
subject="Hello!"
print("From: "+sender,"To: "+recipient,"Subject: "+subject,sep="\n")

#4.25
def vowelCount(string):
    a=0
    e=0
    i=0
    o=0
    u=0
    for n in string:
        if n=="a":
            a+=1
        elif n=="e":
            e+=1
        elif n=="i":
            i+=1
        elif n=="o":
            o+=1
        elif n=="u":
            u+=1
    print("a,e,i,o, and u appear respectively, ",a,",",e,",",i,",",o,",",u," times.")
