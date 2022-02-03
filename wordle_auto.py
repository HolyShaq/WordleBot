import json
import time


# Prunes the word pool based on a letter and its hint
def prune(letter, mode, index):
    # Presence prune - remove words that have the letter
    if mode == "B":
        for _word in word_pool[:]:
            if letter in _word:
                word_pool.remove(_word)
    # Absence prune - remove words that don't have the letter
    #               - remove words that have the letter at the index
    elif mode == "Y":
        for _word in word_pool[:]:
            if letter not in _word:
                word_pool.remove(_word)
            if _word[i] == letter:
                word_pool.remove(_word)
    # Index prune - remove words that don't have the letter at the index
    elif mode == "G":
        for _word in word_pool[:]:
            if _word[index] != letter:
                word_pool.remove(_word)


def hint_validity(string):
    if len(string) == 5:
        if all([letter in "BYG" for letter in string]):
            return True

    print("| Invalid hint!")
    return False


with open("words.json", "r") as f:
    word_pool = json.load(f)

# Main loop
chosen_word = input("Input word to be guessed: ")
tries = 1
hint_string = ""

while True:
    # Get letter frequency in the word pool
    letter_frequency = {}
    [letter_frequency.update({letter: 0}) for letter in "abcdefghijklmnopqrstuvwxyz"]
    for word in word_pool:
        for letter in set(word):
            letter_frequency[letter] += 1

    # Score each word based on letter frequency
    score = lambda w: sum([letter_frequency[letter] for letter in set(w)]) # Sum of the scores of the letters in a word
    word_rank = sorted(word_pool, key=score, reverse=True)

    # Guess the highest ranking word
    print("-------------")
    print("| Based on my calculations, the 3 best words to guess in this case is:")
    for word in word_rank[:3]:
        print(f"|\t{word} - Score: {score(word)}")
    guess = word_rank[0]
    print(f"| So my guess is: {guess}!")

    # Get hints based on guess
    hint_string = ""
    for i, letter in enumerate(guess):
        # Default flag is black
        flag = "B"
        # If letter is present, flag = yellow
        if letter in chosen_word:
            flag = "Y"
            # If letter is in right position, flag = green
            if letter == chosen_word[i]:
                flag = "G"
        hint_string += flag
    print(f"| Hints returned: {hint_string}")
    time.sleep(1)

    if hint_string == "GGGGG":
        print("\n-------------")
        print(f"| Nice! I got the word within {tries} tries!")
        print("-------------")
        break

    # Prune word pool based on hints
    old_word_pool = word_pool[:]
    for i, (letter, hint) in enumerate(zip(guess, hint_string)):
        prune(letter, hint, i)
    print(f"| Removed {len(old_word_pool) - len(word_pool)} words from the word pool!")

    tries += 1
