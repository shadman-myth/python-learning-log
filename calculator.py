# Can use both int & float to get the value of x and y. float includes points and int does not.
x = float (input("Enter the value of x: "))
y = float (input("Enter the value of y: "))
# round(number, ndigits) - number is the number to be rounded and ndigits is the number of decimal places to round to.
z = round(x / y, 2)
# Use : to format the output. The comma is used to separate thousands and .2f is used to round the number to 2 decimal places.
print (f"The value of z is: {z: ,.2f}")