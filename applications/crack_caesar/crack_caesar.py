# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
# Your code here


# read text
with open("ciphertext.txt") as file:
    encrypted_text = file.read()
# perform frequency analysis on string

def func(text):
    letter_count = {}
    for char in text:
        if letter_count[char] in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
            
    print(letter_count)
# decode - sort by value
# apply new values


func(encrypted_text)
