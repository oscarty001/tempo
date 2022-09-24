secret_word = "turtle"

dashes = "_" * len(secret_word)




def update_dashes(secret_word, dashes, guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            dashes = dashes[:i] + guess + dashes[i+1:]
    return dashes


def get_guess():
    while True:
        guess = str(input("Guess: "))
        if len(guess) != 1:
            print("Your guess must have exactly one character!")
        elif not guess.islower():
            print("Your guess must be a lowercase letter!")
        else:
            return guess
            break
        

while True:
    print(dashes)
    guess = get_guess()
    dashes = update_dashes(secret_word, dashes, guess)
    if guess in secret_word:
        print("The character is in the word")
    else:
        print("The character is not in the word")