name = input("What is your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")

elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
# Or use the following code to check if the name is in a list of names

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")