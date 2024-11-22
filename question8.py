import unittest

#to run from terminal (inside folder directory):
#python -m unittest question8.py

# Car interface
class Car:
    def drive(self):
        raise NotImplementedError("You should implement this method.")

# Car classes
class NormalCar(Car):
    def drive(self):
        return "Driving a normal car."

class LuxuryCar(Car):
    def drive(self):
        return "Driving a luxury car."

class SUV(Car):
    def drive(self):
        return "Driving an SUV."

# Car factory
class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "normal":
            return NormalCar()
        elif car_type == "luxury":
            return LuxuryCar()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError("Unknown car type.")
        

# Client code
def main():
    factory = CarFactory()

    # Create various types of cars
    normal_car = factory.create_car("normal")
    luxury_car = factory.create_car("luxury")
    suv = factory.create_car("suv")

    print(normal_car.drive())  
    print(luxury_car.drive())  
    print(suv.drive())    

if __name__ == "__main__":
    main()



######## Test cases for Factory pattern ########

class TestFactory(unittest.TestCase): 

    def test_factory_create_normal(self):
        myFactory = CarFactory()

        normal_car = myFactory.create_car("normal")
        self.assertIsInstance(normal_car, NormalCar)

    def test_factory_create_luxury(self):
        myFactory = CarFactory()

        luxury_car = myFactory.create_car("luxury")
        self.assertIsInstance(luxury_car, LuxuryCar)

    def test_factory_create_suv(self):
        myFactory = CarFactory()

        suv = myFactory.create_car("suv")
        self.assertIsInstance(suv, SUV)