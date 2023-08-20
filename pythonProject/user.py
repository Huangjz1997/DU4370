class user():
    def __init__(self, id, name, stockBookPath, bondBookPath):
        self.id = id
        self.name = name
        self.stockBookPath = stockBookPath
        self.bondBookPath = bondBookPath
        self.isActive = 1

    def getName(self):
        return self.name
