import random


coin = random.choice(["Heads", "Tails"])
print(f"The coin landed on: {coin}")

number = random.randint(1, 100)
print(f"Random number between 1 and 100: {number}")

cards = ["Jack", "Queen", "King", "Ace"]
card_drawn = random.choice(cards)
print(f"You drew a {card_drawn}")

random.shuffle(cards)
for card in cards:
    print(card)

import statistics

print(statistics.mean([100, 250, 325]))