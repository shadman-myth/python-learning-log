def main():
    print_square(3)


def print_square(size):
    for i in range(size): #For each row in square
        for j in range(size): #For each column in square
            print("#", end="") #Prints "#" without moving to the next line
        print()  # Move to the next line after printing a row


main()

#Or you can do this instead:

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)  # Print "#" repeated 'size' times

def print_row(width):
    print("#" * width)  # Print "#" repeated 'width' times

main()