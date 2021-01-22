import random
number = random.randint(0,5)

guess = int(input("I'am thinking about a number (0,5), Can you guess it? "))
while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope Try again:"))
print("well done i was thinking about that, it's ", number)
