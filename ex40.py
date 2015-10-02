import mystuff



class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

#This is what I was trying to do
happy_bday = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]

#this is what I was trying to do
hpbday = Song(happy_bday)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

#this is what I was trying to do
hpbday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# class style
# thing = MyStuff()
# thing.apple()
# print thing.tangerine

# module style
# mystuff.apple()
# print mystuff.tangerine


# dict style
# mystuff = {'apple': "I AM APPLE$S!"}
# print mystuff['apple']




