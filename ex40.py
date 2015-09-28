import mystuff


class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line 

# I want this to do the same thing as bulls_on_parade.sing_me_a_song()
def hbday(i):
    i = ["Happy birthday to you", 
            "I dont want to get sued",
            "So I'll stop right there"]
    return i

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


Song.sing_me_a_song(hbday)


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




