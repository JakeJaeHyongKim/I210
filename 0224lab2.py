text_file=open("top100moviesRT.txt","r")
file_contents=text_file.readlines()
text_file.close()

for i in range(len(file_contents)):
    file_contents[i]=file_contents[i].strip()
print(file_contents)


while True:
    movie=input("Please enter a movie title (or 'stop'):")
    
    if movie in file_contents:
        index_num=file_contents.index(movie)
        print("That's the #", index_num+1, "movie of all time")
    elif movie.lower()=="stop":
        break
    else:
        print("I couldn't find that movie in the list")
