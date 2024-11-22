import unittest

#to run from terminal (inside folder directory):
#python -m unittest question9.py


# Legacy reservation system
class LegacyCarReservationSystem:
    def make_reservation(self, car_type, date):
        return f"Reservation made for a {car_type} on {date} in the legacy system."

# New car sharing system interface
class CarSharingSystem:
    def reserve_car(self, car_type, date):
        raise NotImplementedError("You should implement this method.")

# Adapter class
class LegacySystemAdapter(CarSharingSystem):
    def __init__(self, legacy_system):
        self.legacy_system = legacy_system

    def reserve_car(self, car_type, date):
        return self.legacy_system.make_reservation(car_type, date)


# Client code
def main():
    legacy_system = LegacyCarReservationSystem()

    adapter = LegacySystemAdapter(legacy_system)

    reservation = adapter.reserve_car("SUV", "2024-10-05")
    print(reservation)

if __name__ == "__main__":
    main()




######## Test cases for Adapter pattern ########


class TestAdapter(unittest.TestCase):

    def test_functionality(self):
        #assume
        legacy_system = LegacyCarReservationSystem()
        myAdapter = LegacySystemAdapter(legacy_system)

        # get result from making a reservation
        reservation = myAdapter.reserve_car("SUV", "2024-10-05")
    
        #assert
        self.assertEqual(reservation, "Reservation made for a SUV on 2024-10-05 in the legacy system.")