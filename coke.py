total = 0
while total < 50:
    coin = int(input("Enter the value of the coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        total += coin
        print(f"Amount Due: {50-total}")


print(f"Change Owed: {total-50}")
