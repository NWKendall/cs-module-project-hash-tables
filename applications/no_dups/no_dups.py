def no_dups(s):
    # Your code here
    
    # dict (for lookup time)
    dupes = {}
    # return new arr containing words from str
    if s == "":
        return ""

    str_arr = s.split()
    # create new arr / str
    new_arr = []
    # print("1", str_arr)
    for word in str_arr:
        if word not in dupes:
            # print(word)
            dupes[word] = word
            new_arr.append(word)


    
    # print("DUPES", dupes)

    return " ".join(new_arr)

# check to see if word in dict
    # if not added to dict
# outside for loop ""
# join array


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    # "cats dogs fish"
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))