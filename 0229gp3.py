for i in range(11):
    if i==0:
        for k in range(1,11):
            print(k,end="\t")
        print("*",i,end=" ")
    print(i,end="\t")
    
    for j in range(10):
            print((i)*(j+1), end="\t")
    print()
