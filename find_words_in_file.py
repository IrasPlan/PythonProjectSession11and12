punctuation_remove = (",.!?")
punctuation_space = ("'")


def find_3_letter_words(filename):
    """
    Finds all teh 3 letter words starting with B in a file
    :param filename: the name of the file
    :return: None
    """
    with open(filename) as f:
        # go line by line
        for line in f:
            #replace punctuation in each line
            for p in punctuation_remove:
                line = line.replace(p, "")
            for p in punctuation_space:
                line = line.replace(p, " ")
            words = line.split()
            for word in words:
                if len(word) == 3 and word[0] in "bB":
                    print(word)





find_3_letter_words("input.txt")