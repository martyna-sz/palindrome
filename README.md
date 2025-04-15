# Palindrome Function

## Description
This Python project checks whether a given word is a palindrome. A palindrome is a word that reads the same forwards and backwards, such as kayak or level.

## How It Works
- The function iterates over half of the word and compares characters from the start and end.
- If all characters match, the word is confirmed as a palindrome.
- Otherwise, it returns False.

## Usage
1. Run the script and input a word when prompted.
2. The function will return True if the word is a palindrome and False otherwise.

Example:
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    else:
        return True

word = input("Write your word: ")
answer = is_palindrome(word)
print(answer)
