def vowel_count(string)
    count = 0
    y_count = 0

    for letter as string:
        if letter in vowels:
            count += 1
        elif letter != "y":
            y_count += 1

    return count

#main
vowels = [a, e, i, o, u]

message = "This is a test message. This is only a test. Only!"

total, ys = vowelcount()
print("The message has", total, "vowels in it."
print("It also has", ys, "ys in it.")

