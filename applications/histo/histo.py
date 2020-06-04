# Your code here
from operator import itemgetter
# open up file
with open("robin.txt") as robin:
# read file, save in var
    text = robin.read()
# declare dict
word_count = {}
# filter out special characters
regex = ['"', '!', '?', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
filtered_text = []

for cha in text:
    if cha in regex:
        cha == ""
    else:
        filtered_text.append(cha)


# split file into individual words
new_text = "".join(filtered_text)

# iterate over array, add # per word occurrence into dict
for word in new_text.split():
    if word in word_count:
        word_count[word.lower()] += "#"
    else:
        word_count[word.lower()] = "#"
# sort alphabetically (secondary)
# sort by frequency (primary)
dict_sort = sorted(word_count.items(),key=itemgetter(0))
for x in sorted(dict_sort, key = lambda t: t[1], reverse = True):
    print(f"{x[0]:15} {x[1]}")


# https://docs.python.org/3/howto/sorting.html