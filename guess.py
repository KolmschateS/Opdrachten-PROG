import random

random_num_min = 0
random_num_max = 100000


def guess():
    number = random.randint(random_num_min, random_num_max)
    while True:
        user_input = int(input(f"Guess a number between {random_num_min} and {random_num_max}: "))
        if user_input > random_num_max or user_input < random_num_min:
            print("Not in between parameters!")

        elif user_input > number:
            print("Too high, lower!")

        elif user_input < number:
            print("Too low, higher!")

        else:
            print("Correct, good job")
            break


guess()
