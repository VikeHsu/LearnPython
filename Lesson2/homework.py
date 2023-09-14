import random
random_number = random.randrange(0,100)

while True:
    x = int(input("your_number"))

    if x == random_number:
        print("correct")
        break
    elif x < random_number:
        print("too_small")
    else:
        print("too_big")
print("END")