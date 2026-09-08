class Playlist:
    def __init__(self, Title, Singer, Producer, Song_code):
        self.Title = Title
        self.Singer = Singer
        self.Producer = Producer
        self.__Song_code = Song_code
    def get_title(self):
        return self.Title 
    def check_code(self, code):
        code=int(input("Enter the code to check if the code is correct"))
        if code==self.__Song_code:
            return True
        else:
            return False

