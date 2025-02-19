class Animal:
    def __init__(self,name=None):
        self.num_eyes=2
        self.name=input("what's animal name:")

    def breathe(self):
        print(f"{self.name} inhale,exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print(f'{self.name} moves in water')
    def breathe(self):
        super().breathe()
        print("doing underwater")

fish1=Fish()
fish1.swim()
fish1.breathe()