# Ask for the user's name and capitalize user's name and remove whitespace from str
name = input("What is your name?").strip().title()
# Say hello to the user
print(f"Hello, {name}!")
# Define a function to calculate user''s age based on the year of birth and current year
def calc_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    return age 
birth_year = int(input("Enter your year of birth: "))
this_year = int(input("Enter the current year: "))
# <- store the RETURNED value here
age = calc_age(birth_year, this_year)
print(f"Your age is: {age}")
print(f"Hi {name}, in 10 years you'll be {int(age) + 10}!")
