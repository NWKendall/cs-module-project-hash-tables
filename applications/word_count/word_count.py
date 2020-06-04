import re

def word_count(s):
    # Your code here
    tally = {}
    regex = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    new_str_arr = []

    for c in s:
    # filter special characters
        if c in regex:
            c == ""
        else:
            new_str_arr.append(c)

    # other characters to lowercase
    new_str = "".join(new_str_arr).lower()
    
    # split sting into array
    for word in new_str.split():
        if word in tally:
            tally[word.lower()] += 1
        else:
            tally[word.lower()] = 1

    return tally



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))