rows = eval(input("How many rows should we have?"))
cols = eval(input("How many columns should we have?"))

for i in range(rows):
    print("Row", i, ":", end = '')
    for j in range(cols):
        print(j, end=" ")

    print()
