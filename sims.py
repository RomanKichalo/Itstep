import  random

class Person:
    def __init__(self, name, money, mood, job, car, house, satiety):
        self.name = name
        self.money = money
        self.mood = mood
        self.job.job = job
        self.house = house
        self.satiety = satiety

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

brands_of_car = {
      "BMW":{"fuel": 100, "strength": 100, "consumption": 6},

      "Lada":{"fuel": 50, "strength": 40, "consumption": 10},

      "Volvo":{"fuel": 70, "strength": 150, "consumption": 8},

      "Ferrari":{"fuel": 80, "strength": 120, "consumption": 14}
  }



class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strendt = brand_list[self.brand]["strength"]
        self.strendt = brand_list[self.brand]["consumption"]
