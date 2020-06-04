# Your code here

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
# sort by frequency
# sort alphabetically

dict_sort = sorted(word_count.items(), key = lambda t: t[1], reverse = True)

for x in dict_sort:
    print(f"{x[0]:15} {x[1]}")