from functs import *

print
print('==============================================================================')
sentence = "All good things come to those who are patient and wait. Just let God lead and try to be focused."
print('===Display the whole sentence:===\n',sentence,'\n')
word = break_words(sentence)
print('===Display the words in the sentence separated:===\n',word, '\n')
sortedWords = sort_words(word)
print('===Display the words in the sentence sorted:===\n',sortedWords, '\n')

firstWord = print_first_word(word)
print('\n')
lastWord = print_last_word(word)

sortSentence = sort_sentence(sentence)
print('\n===Display the sentence sorted:===\n',sortSentence, '\n')

print('===Display the first and last word in the sentence:===')
firstlastSentence = print_first_last(sentence)
print('\n')
print('===Display the first and last word in the sorted sentence:===')
sortfirstlastSentence = print_first_last_sorted(sentence)
print('\n')
