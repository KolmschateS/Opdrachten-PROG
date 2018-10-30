def char(low, high):
    for i in range(high - low):
        character = chr(i)
        print(f'{i} : {character}')