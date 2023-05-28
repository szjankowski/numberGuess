
import random

n = random.randrange(1,100)

print("random number within 1,100 range has been generated")
guess = int(input("try to guess it! "))


while n!= guess:
    if guess < n:
        print("It's higer than that")
        guess = int(input("Try again: "))
    elif guess > n:
        print("It's lower than that")
        guess = int(input("Try again: "))
    else:
      break
print("well done, you've guessed correctly!")