from pet import Pet

class Cat(Pet):
    def __init__(self, tricks):
        super().__init__(__name__, tricks)

    def noise(self):
        print("Miaaw!")
        return self