Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #2.11
>>> #A. The sum of negative integers -7 through -1
>>> ((-7)+(-6)+(-5)+(-4)+(-3)+(-2)+(-1))
-28
>>> #B. The average age of a group of kids at a summer camp given that 17 are 9 years old, 24 are 10 years old, 21 are 11 years old, and 27 are 12 years old
>>> (((17*9)+(24*10)+(21*11)+(27*12))/89)
10.651685393258427
>>> #C. 2 to the power -20
>>> (2**-20)
9.5367431640625e-07
>>> #D. The number of times 61 goes into 4356
>>> (4356/61)
71.40983606557377
>>> # E. The remainder when 4365 is divided by 61
>>> (4365%61)
34
>>> #2.14
>>> #A. The first character of string s is 'g'
>>> s="goodbye"
>>> (s[0]=="g")
True
>>> # B. The seventh character of s is 'g'
>>> (s[6]=="g")
False
>>> # C. The first two characters of s are 'g' and 'a'
>>> (s[0]=="g") and (s[1]=="a")
False
>>> # D. The next to last character of s is ' x'
>>> length=len(s)
>>> (s[length]=="x")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    (s[length]=="x")
IndexError: string index out of range
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> (s[5]=="x")
False
>>> # E. The middle character of s is 'd'
>>> (s[4]=="d")
False
>>> (s[3]=="d")
True
>>> # F. The first and last characters of strings are equal
>>> (s[0]==s[6])
False
>>> # G. The last four characters of string s match the string ' tion'
>>> (s[-4]=="tion")
False
>>> (s[-4:]=="tion")
False
>>> # 2.16
# A. Assign 6 to variable a and 7 to variable b.
>>> a=6
>>> b=7
>>> # B. Assign to variable c the average of variables a and b.
>>> c=(a+b)/2
>>> # C. Assign to variable inventory the list containing strings 'paper', 'staples'. and 'pencils'.
>>> inventory=["paper","staples", "pencils"]
>>> # D. Assign to variables first, middle and last the strings 'John', 'Fitzgerald', and 'Kennedy' .
>>> first="John"
>>> middle="Fitzgerald"
>>> last="Kennedy"
>>> # E. Assign to variable fullname the concatenation of string variables first, middle, and last. Make sure you incorporate blank spaces appropriately.
>>> fullname=first+""+middle+""+last
>>> print(fullname)
JohnFitzgeraldKennedy
>>> fullname=first+" "+middle+" "+last
>>> print(fullname)
John Fitzgerald Kennedy
>>> # 2.17
# A. The sum of 17 and -9 is less than 10.
>>> ((17)+(-9)<10)
True
>>> # B. The length of list inventory is more than five times the length of string fullname
>>> (len(inventory)>5*len(fullname))
False
>>> # C. c is no more than 24.
>>> (c<=24)
True
>>> # D. 6.75 is between the values of integers a and b.
>>> (a<6.75) and (b>6.75)
True
>>> # E. The length of string middle is larger than the Iength of string first and smaller than the length string last.
>>> (len(middle)>len(first)) and (len(middle)<len(last))
False
>>> # F. Either the list inventory is empty or it has more than I 0 objects in it.
>>> (len(inventory)==0) or (len(inventory)>10)
False
>>> # 2.18
# A. Assign to variable flowers a list containing strings 'rose'. 'bougainvillea', 'yucca', 'marigold',
# 'daylilly '.and 'lilly of the valley'.
>>> flowers=[rose"
	 
SyntaxError: EOL while scanning string literal
>>> flowers=["rose","bougaivillea","yucca","marigold", "daylilly","lilly of the valley"]
>>> # B. Write a Boolean expression that evaluates to True if string 'potato' is in list flowers, and evaluate the expression.
>>> print("potato" in flowers)
False
>>> # C. Assign to list thorny the sublist consisting of the first three objects in list flowers.
>>> thorny=flowers[0:3]
>>> print(thorny)
['rose', 'bougaivillea', 'yucca']
>>> # D. Assign to list poisonous the sublist consisting of just the last object of list flowers.
>>> poisonous=[flowers[5]]
>>> print(poisonous)
['lilly of the valley']
>>> # E. Assign to list dangerous the concatenation of lists thorny and poisonous.
>>> dangerous=thorny+poisonous
>>> print(dangerous)
['rose', 'bougaivillea', 'yucca', 'lilly of the valley']
>>> # 2.22
# The range of a list of numbers is the largest difference between any two numbers in the list. Write a Python expression that computes the range of a list of numbers 1st. If the list 1st is, say, [3, 7, -2, 12], the expression should evaluate to 14 (the difference between 12 and -2).

>>> 1st=[3,7,-2,12]
SyntaxError: invalid syntax
>>> lst=[3,7,-2,12]
>>> minVal=min(lst)
>>> maxVal=max(lst)
>>> print(maxVal-minVal)
14
>>> # 2.28
# A. An expression that evaluates to the index of the middle element of lst
>>> (len(lst)/2)
2.0
>>> # B. An expression that evaluates to the middle element of 1st
>>> print(lst[int(len(lst)/2)])
-2
>>> # C. A statement that sorts the list 1st in descending order
>>> print(sorted(lst, reverse=True))
[12, 7, 3, -2]
>>> # D. A statement that removes the first number of list lst and puts it at the end
>>> lst.append(lst.pop())
>>> print(lst)
[3, 7, -2, 12]
>>> 
