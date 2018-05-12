def open_file():
    while True:
        try:
            valid=str(input("Please enter a filename:"))
            filename=valid+".txt"
            file=open(filename)
        except:
            print("That's not valid")
        else:
            contents=file.read()
            contents=contents.split("\n")
            file.close()
            print(contents)
            break
        

#main

open_file()
print("The contents of the file:")
