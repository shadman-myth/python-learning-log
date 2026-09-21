s = input("Camel case: ")
result = ""
for c in s:
    if c.isupper():
        result += "_" + c.lower()
    else:
        result += c
print("Snake case:",result)
