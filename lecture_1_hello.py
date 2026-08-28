# Ask for the user's name
name = input("What is your name?")
# Remove whitespace from str
name = name.strip()
# Capitalize the first letter of the name
name = name.capitalize()
# Capitalize user's name
name = name.title()
# Remove whitespace from str and capitalize user's name
name = name.strip().title()
#Split the name into first and last name
first_name, last_name = name.split(" ")
# Say hello to the user
print(f"Hello, {first_name}")
