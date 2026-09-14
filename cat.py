i = 3
while i != 0:
    print("meow")
    i = i - 1
#Other method to do this is:
i = 0
while i < 3:
    print("meow")
    i += 1
#Other method to do this is:
for i in [0, 1, 2]:
    print("meow")
#Other method to do this is:
for i in range(3):
    print("meow")
#This is better
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for i in range(n):
    print("meow")

#Or define a separate function to do this
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for i in range(n):
        print("meow")

main()           