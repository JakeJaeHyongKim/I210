#3.20 <For Loop, printing 3 characters>
lst=["January","February","March"]
for char in lst:
    print (char[:3])
#3.21 <For loop, even number in list>
for i in range(2,9):
    if i%2==0:
        print(i)
#3.23 <For loop, range() sequences>
#a
for i in range(2):
    print(i)
#b
for i in range(1):
    print(i)
#c
for i in range(3,6):
    print(i)
#d
for i in range(1,2):
    print(i)
#e
for i in range(0,4,3):
    print(i)
#f
for i in range(5,22,4):
    print(i)
#3.25 <a list of student names>
stu_name=eval(input("Enter list:"))
for char in stu_name:
    if char[0] in "abcdefghijklmABCDEFGHIJKLM":
        print(char)
#3.33 <reverse_string(), 3 letter string and return reversed>
string=input("Enter a string: ")
def reverse_string(string):
    b = "".join(sorted(string, reverse=True))
    return (b)
#main
print (reverse_string(string))

#3.35 <probability coin>
number=eval(input("Enter a number: "))
def prob(number):
    if number>0:
        return 2**-number
#main
print(prob(number))

#3.41 <two strings form, first and last name>
FirstName=input("Enter your first name:")
LastName=input("Enter your last name:")
def lastF(FirstName,LastName):
    return LastName+","+FirstName[0].upper()
#main
print(lastF(FirstName,LastName))
#3.44 <distance(), speed of sound>
sound=eval(input("Enter the time elapsed")
def distance(sound):
           return sound*340.29/1000
print(distance(sound))
#additional <Random Cinema, random movies>
import random
movies=input("Enter list of words:")
numMovies=eval(input("Please enter a number of movies you'd like to generate:"))
print("Welcome to Randoplex! Currently playing movies are:")
def choice(movies):
    for i in range(0, numMovies):
        return random.choice(movies)+" "+random.choice(movies)+" "+random.choice(movies)
#main
print(choice(movies))
