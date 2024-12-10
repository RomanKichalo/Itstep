
class Human:
    height = 170

    def __init__(self):
          self.height = 150

class Student(Human):
    def __init__(self):
        print(self.height)

        super().__init__()
        print(self.height)
        print(super().height)

class Worker(Human):
    pass

nick = Student()
ann = Worker



















class Computer():
    def caculate(self):
        print("Calculating...")

class Display:
    def display(self):
        print("zzzzzzz")

class SmartPhon(Computer, Display):
    pass

iphon = SmartPhon()

iphon.display()
iphon.caculate()







class AudioPlayer:
    def play_audio(self):
        print("Відтворюється аудіо")

class VideoPlayer:
    def play_video(self):
        print("Відтворюється відео")

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def play(self):
        print("Відтворюється мультимедійний вміст")



multimedia_player = MultimediaPlayer()
multimedia_player.play()
multimedia_player.play_video()

























