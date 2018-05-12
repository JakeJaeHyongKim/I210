# Table Print v2

def table_print(headers, data,padding):

    print(headers[0],headers[1],headers[2],sep="\t")

    print("-"*25)

    for i in range(len(data)):
        print(i, data[i][0],data[i][1],sep="\t")


    # Add your code here!

    # Nothing else in the file should change

#main - Don't change this part!
labels = ["i", "Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores)

labels = ["i", "Capital", "State"]
scores = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels, scores)
