import random


def dice_throw():
    dubbel = 0
    while dubbel != 2:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        throw = dice1 + dice2
        if dice1 == dice2:
            print(f'{dice1} + {dice2} = {throw} (Dubbel)')
            dubbel += 1

        else:
            print(f'{dice1} + {dice2} = {throw}')
            break
    else:
        print(f'{dice1} + {dice2} = {throw} , Naar de gevangenis gauw!')


dice_throw()