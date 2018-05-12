def vowel_count(string):
    
    #begin count with 0
    count = 0
    y_count = 0
    #vowels list
    vowels = ["a","e", "i", "o","u"]
    
    for letter in string:
        #every letter that is in vowels list
        if letter in vowels:
            count += 1
            
        #every letter that is equal to "y"
        elif letter=="y":
            y_count += 1
        #always else loop when if loop is used
        else:
            count+=0
            y_count+=0

    #only 1 can be returned, otherwise delet previous var. (So can be returned as tuple)
    return count,y_count

#main

message = "This is a test message. This is only a test. Only!"
#same order with return, one goes to first the other goes to second
count,y_count=vowel_count(message)
print("The message has", count, "vowels in it.")
print ("It also has", y_count, "ys in it.")
