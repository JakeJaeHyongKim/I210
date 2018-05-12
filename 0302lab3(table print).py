import tools
#Very good way
def counterList(listNum):
    dict={}
    for num in listNum:
        if not num in dict:
            dict[num]=1
        else:
            dict[num]=dict[num]+1
    tools.table_print(["number","count"], dict.items(),10)
        
#    print("Number \t Count")
#    print("-"20)

#   for elem,val in sorted(dict.items()):
#        print(elem,"\t\t",val)

counterList([5,5,6,6,7,7,7,7,7,8,9,10,10,10])
