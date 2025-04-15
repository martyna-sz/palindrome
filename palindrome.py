def is_palindrome(word):
    word = word.lower().replace(" ","")
    for i in range(len(word) // 2):
        if word[i] != word[len(word)-i-1]:
            return False
    else:
        return True
word = input("write your word ")
answer = is_palindrome(word)
print(answer)