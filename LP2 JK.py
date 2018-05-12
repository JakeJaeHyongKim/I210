import tools

#sect 1


#choice of file
def loadFile():
    file_choice=str(input("Which state's totals would you like to compute?"))
    file_txt=file_choice+".txt"
    file=open(file_txt,"r")
    contents=file.readlines()
    
    #dictionary form

    dic_list={}
    #sum votes up process
    total=0

    file.close()
    
    #clean up and sum votes to total
    for elem in contents:
        contentsSplit=elem.strip().split("\t")
        if not contentsSplit[0] in dic_list:
            dic_list[contentsSplit[0]] = int(contentsSplit[1])
            total+=int(contentsSplit[1])
        else:
            dic_list[contentsSplit[0]] = int(dic_list[contentsSplit[0]]) + int(contentsSplit[1])
            total+=int(contentsSplit[1])
            
    # Will store the sorted array
    sorted_dic=[]
    # Stores things already added to the sorted Array for increase efficiency
    comp_dic=[]
     # Tracks percentages to print later
    perc_track=[]
    
    for elem, key in dic_list.items():
        
        # Reset every time before looping to find max
        largestElem = [0,0]
        
        for elem_2, key_2 in dic_list.items():

            # if it is larger than current max and not already added into master array
            if key_2 > largestElem[1] and not elem_2 in comp_dic:
                largestElem = [elem_2, key_2]

        comp_dic.append(largestElem[0])

        # Some magic to make percentages look nice
        perc_track.append([largestElem[0], str(round((largestElem[1] / total) * 100,2))+"%"])

        sorted_dic.append(largestElem)
        
    print("The candidate earned this many votes:")
    tools.table_print(["Name","Votes"],sorted_dic,15)

    print("The breakdown by percent:")
    tools.table_print(["Name","Percentage"],perc_track,15)

#repeat until stop
    while True:
        var = str(input("Which state's totals would you like to compute? (or STOP)"))
        if var.lower()=="stop":
            break
        else:
            loadFile(var)
    return loadFile(file_txt)
