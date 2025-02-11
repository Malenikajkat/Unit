class Car:
    def __init__(self, color, num_wheels):
        self.color = color
        self.num_wheels = num_wheels

    def going(self):
        print(f"{self.color} едет")


my_car = Car("red", 4)
my_car.going()
you_car = Car("blue", 4)
you_car.going()


