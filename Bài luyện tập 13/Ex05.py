class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def __str__(self):
        return f'Hoa {self.name} co mau {self.color}'

f = Flower('Hong', 'Do')
print(f)