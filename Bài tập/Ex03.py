class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def set_name(self, name):
        self._name = name
    def set_price(self, price):
        self._price = price
vd1 = Book('Novel', 200)
print('Gia: ', vd1.get_price())