def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0:2] .isalpha():
        return False
    digit_found = False
    for c in s:
        if c.isdigit():
            if not digit_found and c == "0":
                return False
            digit_found = True
        elif digit_found:
            return False

    return True

main()