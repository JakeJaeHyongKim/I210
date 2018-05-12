# functions
def paren_checker(lines, count):
    if not lines and count==0:
        return True
    elif not lines:
        return False
    elif lines[0]=="(":
        count=count+1
        return paren_checker(lines[1:], count)
    elif lines[0]==")":
        count=count-1
        return paren_checker(lines[1:], count)
        

    

# main
while True:
    while True:
        user_file = input("Which file would you like to open?")+".txt"
        try :
            file=open(user_file,"r")

        except:
            print("That isn' a valid file")

        else:
            contents=file.readlines()
            for i in range(len(contents)):
                contents[i]=contents[i].strip()
            file.close()
            break
            
            


    valid = paren_checker(contents, 0)

    if valid:
        print("The parentheses match!\n")
    else:
        print("The parentheses don't match!\n")
    
    repeat=str(input("Would you like to check another file? (Y/N)")).title()

    if "Y" in repeat:
        print(input("Which file would you like to open?")+".txt")
    else:
        break

# Put some code here to repeat the process if the user wants



