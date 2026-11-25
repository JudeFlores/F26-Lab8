#Making my favorite object
class topspinner:
    def __init__(self, color, material, price):
        self.color = color
        self.material = material
        self.price = price

    def describe(self):
        print(f"This top is {self.color}, {self.material}, ${self.price}")

    def spin(self, rpm):
        print(f"The top is spinning at {rpm}rpm")
