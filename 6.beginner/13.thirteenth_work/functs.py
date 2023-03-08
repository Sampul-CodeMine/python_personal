def break_words(stuff):
    # this function will break words for us
    words = stuff.split(' ')
    return words


def sort_words(words):
    # this function will sort words
    return sorted(words)


def print_first_word(words):
    # prints the first word after popping it off
    word = words.pop(0)
    print ('The first word in the sentence is:\n',word)


def print_last_word(words):
    word = words.pop(-1)
    print ('The last word in the sentence is:\n',word)


def sort_sentence(sentence):
    """Takes a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
