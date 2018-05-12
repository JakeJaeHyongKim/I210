text=open("top100moviesAFI.txt","r")

set1=set(text.readlines())
text.close()

text1=open("top100moviesRT.txt","r")

set2=set(text1.readlines())
text1.close()

for movie in set1&set2:
    print(movie.strip())
