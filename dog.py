from pet import Pet

class Dog(Pet):
    def __init__(self, tricks):
        super().__init__(__name__, tricks)

    def noise(self):
        print("Wouuf!")
        return self