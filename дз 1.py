import random
import time

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.age = 0
        self.happiness = 50
        self.hunger = 50
        self.energy = 50

    def feed(self):
        if self.hunger < 100:
            self.hunger += 20
            print(f"{self.name} поїв і почувається краще!")
        else:
            print(f"{self.name} вже не голодний!")

    def play(self):
        if self.energy > 20:
            self.happiness += 10
            self.energy -= 20
            print(f"{self.name} грається і радіє!")
        else:
            print(f"{self.name} занадто втомлений для гри.")

    def sleep(self):
        self.energy = 100
        self.happiness += 5
        print(f"{self.name} спить і відновлює сили!")

    def age_one_year(self):
        self.age += 1
        self.hunger -= 10
        self.energy -= 10
        self.happiness -= 5
        print(f"{self.name} став старший на один рік!")

    def check_status(self):
        print(f"\nСтатус {self.name}:")
        print(f"Вік: {self.age} років")
        print(f"Щастя: {self.happiness}/100")
        print(f"Голод: {self.hunger}/100")
        print(f"Енергія: {self.energy}/100")

    def interact(self):
        actions = ["feed", "play", "sleep", "age_one_year"]
        action = random.choice(actions)
        if action == "feed":
            self.feed()
        elif action == "play":
            self.play()
        elif action == "sleep":
            self.sleep()
        elif action == "age_one_year":
            self.age_one_year()

pet = Pet("Борис", "кіт")

for _ in range(5):
    time.sleep(1)
    pet.interact()
    pet.check_status()
