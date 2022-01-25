import json
import random


def check_word_validity(word):
    if len(word) != 5:
        print("~Five letter words only~")
        return False
    if word not in allowed_words:
        print("~Invalid word~")
        return False

    return True


# Load json files
with open("words.json", "r") as f:
    word_list = json.load(f)

with open("allowed_words.json", "r") as f:
    allowed_words = json.load(f)

# Choose random word from word list
chosen_word = random.choice(word_list)
print(chosen_word)

# Main loop
tries = 1
while True:
    print(f"Try #{tries}")
    guess = input("Guess: ").lower()
    valid = check_word_validity(guess)

    while valid is not True:
        guess = input("Guess: ").lower()
        valid = check_word_validity(guess)

    # Check word
    hint = ""
    for i, letter in enumerate(guess):
        # Default flag is black
        flag = "B"

        # If letter is present, flag = yellow
        if letter in chosen_word:
            flag = "Y"

            # If letter is in right position, flag = green
            if letter == chosen_word[i]:
                flag = "G"

        hint += flag

    if hint != "GGGGG":
        tries += 1
        if tries == 7:
            print("\nToo many tries! The word is", chosen_word)
            print("Better luck next time!")
            break
    else:
        print("\n Correct! The word is", chosen_word)
        print(f"You got it in {tries} tries!")
        break

    print("Hint: ", hint)