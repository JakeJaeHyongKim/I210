while True:
    try:
        num=int(input("Enter an integer:"))
    except:
        print("That wasn't an integer.")
    else:
        print("integer entered.")
        break
