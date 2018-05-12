grades = {"Sam": 90, "Ali": 92, "Dave": 85, "Pat": 81}

person = input("Whose grade do you want to know? ")

if person in grades:
    print(person, "got a", grades[person])
else:
    print("They got a 0 for not turning in their work.")

