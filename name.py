import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments provided. Please provide at least one argument.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments provided. Please provide only one argument.")
else:
    print("Hello, my name is", sys.argv[1])
#Write your name or arguments in the terminal to see the output. name.py or the name of the file is an argument aswell.

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)