import mystuff


class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line 

def hbday(i):
    Song = ["Happy birthday to you", 
            "I dont want to get sued",
            "So I'll stop right there"]
    return Song

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


hbday.sing_me_a_song()


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




