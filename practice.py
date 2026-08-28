def calc_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    print(f"You're currently {age} years old.")

birth_year = int(input("Enter your year of birth: "))
this_year = int(input("Enter the current year: "))
calc_age(birth_year, this_year)
# to bring out a square of a number
def main():
    x = int(input("Enter the value of x: "))
    print(f"The square of {x} is:", square(x))


def square (n):
    return pow(n, 2)

main()