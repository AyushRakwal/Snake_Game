class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale , exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Moving in e-water")    

    def swim(self):
        print("I live in water")



crown = Fish()
crown.breathe()
crown.swim()
print(crown.eyes)            