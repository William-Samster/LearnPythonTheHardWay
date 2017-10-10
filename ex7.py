#this is the 7th exercise from the book
# this is about various ways of printing

print("Mary had a little lamb")
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that mary went")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

#this is the 8th exercise of the book about more complex printing

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "This is the first statemen\n",
    "This is the second statement\n",
    "This is the third statement\n",
    "This is the fourth statement\n",
))

#This is the 9th exercise of the book about even more complex printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
print("Here are the days", days)
print("Here are the months", months)
print("""
    This is a long paragraph
    that will span across multiple
    lines and will show how to write
    a paragraph
    """
)


#this is the 10th exercise of the book about some more advanced formatting

tabby_cat = "\t I am tabbed in"
persian_cat = "I am split\non a line"
backslash_cat = "I'm a \\ a \\ cat"
fat_cat = """
I'll do a list
\t* cat fish
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
