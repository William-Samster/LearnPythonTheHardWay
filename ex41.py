# this is the 41th exercise of the book and is about practising classes
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "ClassX(Y):" :
        "Make a class named X that is-a Y",

    "classX(object):\n\t def __init__(self, J)":
        "Class X has-a __init__ that takes self and J params.",

    "classX(object):\n\t def __init__(self, J)":
        "class X has-a function that takes self and J as params",

    "foo = X():"
        "set foo to an insance values of foo"

    "X.__init__(J)": "From X get-the function __init__ and call it with param self and J"

    "X.Y = 'Z'": "From X get the attribute Y and set it to Z"

}
