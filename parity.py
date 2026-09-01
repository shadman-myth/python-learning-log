x = int(input("Enter the value of x: "))

if x % 2 == 0:
    print(f"{x} is an even number")
else:
    print(f"{x} is an odd number")
# You can use either of these two methods to check if a number is even or odd. The first method uses the modulus operator (%) to check if the remainder of x divided by 2 is 0. If it is, then x is even; otherwise, it is odd. The second method uses a function called is_even() that takes an integer n as an argument and returns True if n is even and False if n is odd.
def main():
    x = int(input("Enter the value of x: "))
    if is_even(x):
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")

def is_even(n):
    return n % 2 == 0
main()