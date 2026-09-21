class Media:
    def play(self):
        print("Playing media")


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


# Create objects
media_list = [Audio(), Video(), Podcast()]

# Same method called for different objects
for media in media_list:
    media.play()