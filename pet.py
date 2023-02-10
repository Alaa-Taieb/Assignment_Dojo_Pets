class Pet:
    def __init__(self, type, tricks):
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    
    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise():
        pass
