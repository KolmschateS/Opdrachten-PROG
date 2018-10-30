def computer_guess(num):
    low = 1
    high = 100000000
    guess = 50
    while guess != num:
        guess = (low + high) // 2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")


def main():
    low = 1
    high = 100000000
    num = int(input("Enter a number: "))
    if num < low or num > high:
        print(f"Must be in range [{low}, {high}]")
    else:
        computer_guess(num)


if __name__ == '__main__':
    main()
