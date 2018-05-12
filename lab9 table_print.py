# Table Print v2

def table_print(headers, data):



    print('{0}  {2} {1}'.format(*headers))

    for i in range(len(data)):
        print(str(i), data[i][0], data[i][1], sep="\t")



#main - Don't change this part!
labels = ["i", "Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores)

labels = ["i", "Capital", "State"]
scores = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels, scores)
