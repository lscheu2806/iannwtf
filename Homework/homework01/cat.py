class Cat:
    def __init__(self, name):
        self.name = name
    
    def greet(self, other):
        if(isinstance(other, Cat)):
            print(f"Hi, I'm {self.name}! I see you are also a Cat, {other.name}.")