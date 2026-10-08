class Song_stats:
    def __init__(self, Title, Singer, Producer, Song_code):
        self.Title = Title
        self.Singer = Singer
        self.Producer = Producer
        self.__Song_code = Song_code
    def get_title(self):
        return self.Title 
    def get_singer(self):
        return self.Singer
    def get_Producer(self):
        return self.Producer
    def get_code(self):
        return self.__Song_code
    def check_code(self):
        code=int(input("Enter the code to check if the code is correct"))
        if code==self.__Song_code:
            return True
        else:
            return False
    def change_code(self):
        while True:
            old_code=int(input("Enter the old code to verify user identity"))
            if (old_code==self.__Song_code):
                new_code=int(input("What is the new 8 digit code you wish to use?"))
                if (10000000<=new_code<=99999999):
                    self.__Song_code=new_code
                    print("Code updated successfully!")
                    break
            else:
                print("Update failed, recheck if code contains 8 digits and matches the old code")

Mahika=Song_stats("Mahika", "Adie", "Adie", 23147593)
Paraluman=Song_stats("Paraluman", "Adie", "Adrian Garcia", 54231428)

print("Mahika's code:", Mahika.get_code())
print("Paraluman's code:", Paraluman.get_code())

print("")
Mahika.change_code()
print("")

print("Mahika's code:", Mahika.get_code())
print("Paraluman's code:", Paraluman.get_code())

