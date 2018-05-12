text_file=open("professions.txt","r")
#read each lines in text_file, different with .read()
file_contents=text_file.readlines()
text_file.close()

#new list called lst
lst=[]

#for loop for every item in file contents
for i in file_contents:
    
    #append strip splited by ", " to list
    lst.append(i.strip().split(", "))
    print(i.strip().split(", "))
    
#close text_file that opened
text_file.close()

#print empty line
print()

#print list in new line
print("All the data:","\n",lst)
