lion=Lion("Simba")
elephant=Elephant("Dumbo")
monkey=Monkey("George")

class Animal:
    def __init__(self,name,make_sound):
        self.name=name
        self.make_sound=make_sound

    def eat(self,name):
        print(self.name, "eats.")

    def make_sound(self,name):
        print(self.name, "makes a sound!")

class Lion(Animal):
    def __init__(self,name,make_sound):
        super().__init__(name, make_sound)
    
    def eat(self, name):
        print(self.name, "eats fresh meat.")

    def make_sound():
        print(self.name, "roars loudly!")

class Elephant(Animal):
    def __init__(self,name,make_sound):
        super().__init__(name, make_sound)
    
    def eat(self, name):
        print(self.name, "eats grass and fruits.")

    def make_sound():
        print(self.name, "trumpets!")

class Monkey(Animal):
    def __init__(self,name,make_sound):
        super().__init__(name, make_sound)
    
    def eat(self, name):
        print(self.name, "eats bananas.")

    def make_sound():
        print(self.name, "chatters!")

