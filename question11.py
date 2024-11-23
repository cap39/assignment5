class APIGateway:
    def __init__(self):
        self.ride_matching_service = RideMatchingService()
        self.billing_service = BillingService()
    def add_driver(self, driver):
        self.ride_matching_service.add_driver(driver)
    def add_rider(self, rider):
        self.ride_matching_service.add_rider(rider)
    def request_ride(self):
        return self.ride_matching_service.match_ride()
    def calculate_and_bill(self, rider, distance):
        fare = self.billing_service.calculate_fare(distance)
        return self.billing_service.process_payment(rider, fare)
    
class BillingService:
    def calculate_fare(self, distance):
        fare_rate = 0.83
        return round(distance * fare_rate, 2)

    def process_payment(self, rider, fare):
        return f"Processed payment of ${fare} for {rider}"

class RideMatchingService:
    def __init__(self):
        self.drivers = []
        self.riders = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_rider(self, rider):
        self.riders.append(rider)

    def match_ride(self):
        if not self.drivers or not self.riders:
            return "No matches available"
        driver = self.drivers.pop(0)  # Match the first available driver
        rider = self.riders.pop(0)   # Match the first rider in queue
        return f"Matched Driver {driver} with Rider {rider}"



# Test case #2
# When there is a driver but no rider available 
api_gateway = APIGateway()
api_gateway.add_driver("Driver")
assert api_gateway.request_ride() == "No matches available", "Test case #2 failed!"
print("Question 11 test passed")

