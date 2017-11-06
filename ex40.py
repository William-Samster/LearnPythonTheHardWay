# This is the 40th exercise of the book and its about classes


class song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_birthday = song(["Happy birthday to you"
                       "I don't want to get sued"
                       "So I will stop here."
                       ])

bulls_on_parade = song(["They rally around the family"
                        "with pocket full of shells"
                        ])

happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
