import random

text=open("top100moviesAFI.txt","r")

set1=set(text.readlines())
text.close()

text1=open("top100moviesRT.txt","r")

set2=set(list(text1.readlines()))
text1.close()



mar=eval(input("How many movies in your marathon?:"))
for i in range(mar):
    print(random.choice(set1&set2))
print("Your custom",mar,"movie marathon:")


set1.remove(set1&set2)

print(movie.strip())
