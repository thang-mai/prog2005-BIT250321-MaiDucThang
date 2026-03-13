class Product:
    def __init__(self, price):
        self.set_price(price)
    def get_price(self):
        return self._price
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print('Gia phai lon hon 0')
    def __str__(self):
        return f'Product price: {self._price}'
p = float(input('Nhao gia san pham: '))
product = Product(p)
print(product)