# Parent Class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.level = level

    def use_power(self):
        print(f"{self.name} uses {self.power} at level {self.level}!")

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up to level {self.level}!")

# Child Class (Inheritance + Polymorphism)
class Villain(Superhero):
    def use_power(self):
        print(f"{self.name} unleashes evil {self.power} at level {self.level}... Muhahaha!")

# Create objects
hero = Superhero("Stormblade", "Lightning Strike", 5)
villain = Villain("Darkshade", "Shadow Flame", 6)

# Call methods
hero.use_power()
hero.level_up()

villain.use_power()
villain.level_up()
