# Definition of the class "Fish"
class Fish:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def swim(self):
        print(f"{self.name} is swimming forward.")

# Creating instances of the Fish class
nemo_fish = Fish("Nemo", "orange")
douglas_fish = Fish("Douglas", "blue")

# Calling the swim method for two fish
nemo_fish.swim()
douglas_fish.swim()
# Definition of the class "Shark" as a subclass of Fish
class Shark(Fish):
    def __init__(self, name, color, size):
        super().__init__(name, color)
        self.size = size
    
    def hunt(self):
        print(f"{self.name} starts hunting.")

# Creating an instance of the Shark class
jack_shark = Shark("Jack", "gray", "large")

# Using methods from the base class and new methods
jack_shark.swim()
jack_shark.hunt()
# Definition of a function that calls the swim method on any object
def make_swim(aquatic_creature):
    aquatic_creature.swim()

# Using the function with different objects
make_swim(nemo_fish)
make_swim(jack_shark)
# Definition of a class with private attributes
class SeaMonster:
    def __init__(self, name, strength):
        self.__name = name
        self.__strength = strength
    
    def attack(self):
        print(f"{self.__name} attacks with strength {self.__strength}.")

# Creating an instance of the SeaMonster class
kraken_monster = SeaMonster("Kraken", 1000)

# Attempt to directly access private attributes
try:
    print(kraken_monster.__name)
except AttributeError as e:
    print(e)

# Using a public method to interact with the object
kraken_monster.attack()
