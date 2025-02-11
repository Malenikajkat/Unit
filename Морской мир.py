import random

# Definition of the class "Aquatic Creature"
class AquaticCreature:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    
    def swim(self):
        print(f"{self.name} is swimming forward.")
    
    def attack(self, target):
        if isinstance(target, AquaticCreature):
            damage = random.randint(10, 30)
            target.health -= damage
            print(f"{self.name} dealt {target.name} {damage} damage.")
            if target.health <= 0:
                print(f"{target.name} has died.")
        else:
            print(f"{target.name} is not an aquatic creature and cannot be attacked.")

# Definition of subclasses
class Fish(AquaticCreature):
    pass

class Shark(AquaticCreature):
    def __init__(self, name, health=150):
        super().__init__(name, health)

# Creating characters
nemo_fish = Fish("Nemo", 50)
jack_shark = Shark("Jack")

# Start of the game
while nemo_fish.health > 0 and jack_shark.health > 0:
    choice = input("Choose an action: 1 - Nemo attacks Jack, 2 - Jack attacks Nemo: ")
    if choice == '1':
        nemo_fish.attack(jack_shark)
    elif choice == '2':
        jack_shark.attack(nemo_fish)
    else:
        print("Invalid choice.")

if nemo_fish.health <= 0:
    print("Nemo lost.")
else:
    print("Jack lost.")
