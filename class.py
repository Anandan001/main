class Car:
    # Constructor to initialize attributes
    def __init__(self, make, model, year,rate,a):
        self.make = make  # Instance attribute
        self.model = model
        self.year = year
        self.rate=rate
        self.a=a

    # Method to display information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
        print("rate=",self.rate+self.year)

    # Method to simulate starting the car
    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine is now running.")
    def print_a(self):
        print(self.make)
    def print_b(self):
        print(self.rate+self.a)


# Create an object (instance) of the Car class
my_car = Car("Tesla", "Model S", 2022,20000,5)

# Accessing attributes and methods
my_car.display_info()  # Output: 2022 Tesla Model S
my_car.start_engine()  # Output: The Tesla Model S's engine is now running.
my_car.print_a()
my_car.print_b()
