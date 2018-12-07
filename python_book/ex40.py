class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you", "Seoncd line of the song"])

bulls_on_parade = Song(["They rally round the family",
                        "with pockets full of shells"])

happy_bday.sing_a_song()

bulls_on_parade.sing_a_song()
