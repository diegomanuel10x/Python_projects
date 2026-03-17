class Car():
    def __init__(self, model, colour, year):
        self.model = model
        self.colour = colour
        self.year = year

    def build(self):
        print(f"My car is a {self.model} and it is coloured {self.colour}, I built it back in {self.year}")

car = Car("Toyota", "Green", 2017)

car.build()