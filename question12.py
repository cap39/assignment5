import datetime
from enum import Enum
from typing import List, Optional


# models
class RideStatus(Enum):
    REQUESTED ="REQUESTED"
    ACCEPTED = "ACCEPTED"
    IN_PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
class Driver:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.review_score = 5.0
        self.available = True
class Ride:
    def __init__(self, id: int, user: User):
        self.id = id
        self.user = user
        self.driver: Optional[Driver] = None
        self.status = RideStatus.REQUESTED
        self.timestamp = datetime.datetime.now()

#Controllers
class RideController:
    def __init__(self):
        self.rides: List[Ride] = []
        self.ride_counter = 0

    def schedule_ride(self, user: User) -> Ride:
        self.ride_counter += 1
        ride = Ride(self.ride_counter, user)
        self.rides.append(ride)
        return ride
    
    def update_ride_status(self, ride: Ride, status: RideStatus, driver: Driver = None):
        ride.status = status
        if driver:
            ride.driver = driver

class DriverApp:
    def __init__(self, ride_controller: RideController):
        self.ride_controller = ride_controller
    def accept_ride(self, ride: Ride, driver: Driver):
        print(f"\nDriver {driver.name} accepting ride{ride.id}...")
        self.ride_controller.update_ride_status(ride, RideStatus.ACCEPTED, driver)
        print(f"Ride #{ride.id} accepted by driver {driver.name}")
    


class UserApp:
    def __init__(self, ride_controller: RideController):
        self.ride_controller = ride_controller
    def request_ride(self, user: User):
        print(f"\nUser {user.name} requesting ride...")
        ride = self.ride_controller.schedule_ride(user)
        print(f"Ride #{ride.id} scheduled at {ride.timestamp}")
        return ride
    


# Test case #3:
# Double ride acceptance
def main():
    ride_controller = RideController()
    user_app = UserApp(ride_controller)
    driver_app =DriverApp(ride_controller)
    user = User(1, "Alice")
    driver = Driver(1, "Bob")
    ride = user_app.request_ride(driver)
    driver_app.accept_ride(ride, driver)
    driver_app.accept_ride(ride, driver)
    assert ride_controller.ride_counter == 1, f"Ride counter is supposed to be 1 but it is {ride_controller.ride_counter}"
	print("question 12 test passed")

main()