#this is the 25th exeercise of the book and more practice of what
#i have learnt

#this fucntion with break the word for us
def break_words(stuff):
    words = stuff.split()
    return words

#this fucntion will sort the words for us
def sort_words(words):
    return sorted(words, key=str.lower)

#this fucntion will print the firs words
def print_first_word(words):
    word = words.pop(0)
    print(word)

#this prints the last word after popping it

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    word = break_words(sentence)
    sortedword = sort_words(word)
    print(sortedword)
    return sortedword

#this function will print first and the last word of the sentence
def print_first_and_last_sentence(sentence):
    word = break_words(sentence)
    print_first_word(word)
    print_last_word(word)

def print_first_and_last_sorted(sentence):
    word = break_words(sentence)
    sword = sort_words(word)
    print_first_word(sword)
    print_last_word(sword)


if __name__ == '__main__':
    sentence = "All good things come to those wo wait"
    print break_words(sentence)
