class Human:
    def __init__(self, name):
     self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passengers in args:
            self.passengers.append(passengers)

    def print_passengers_name(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"There are no passegers in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
roman = Human("Roman")
dog = Human("Dog")

car = Auto("Mersedes")


car.add_passengers(nick, kate, roman, dog)

car.print_passengers_name()












































