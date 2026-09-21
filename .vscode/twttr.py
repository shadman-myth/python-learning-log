s = input("Input: ")
result = ""
for c in s:
    if c.lower() not in "aeiou":
        result += c
print("Output:", result)