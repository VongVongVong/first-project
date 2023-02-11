class Car:
    amount_of_cars = 1

    def __init__(self,brand="mers", cost=50, licence_plate="ih2p5", color="Blue", model=1):
        self.cost = cost
        self.total_value = cost*1000
        self.color = color
        self.brand = brand
        self.licence_plate = licence_plate
        self.model = model
        Car.amount_of_cars += 1

    def __str__(self):
        return f"{self.brand} is ${self.cost}/per day"


    def __del__(self):
        print( f"the {self.color} {self.brand} {self.model} is sold")


    def rent_out(self):
        self.total_value = self.total_value - (self.cost * 0.1)
        print(f"{self.brand} rented out")




first_car = Car()

second_car = Car("toyota", 35, "b45ol", "Yellow", 2)


print(first_car)

print(Car.amount_of_cars)
