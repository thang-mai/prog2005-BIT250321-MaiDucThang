class User:
    def __init__(self, id):
        self.id = id
    @property
    def id(self):
        return self.id
u = User(101)
print(u.id)