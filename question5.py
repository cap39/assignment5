import unittest

#to run from terminal (inside folder directory):
#python -m unittest question5.py

class RushHourStrategy:
    def calculate_fee(self, base_fare, distance, supply, demand): 
        multiplier = 1.5
        surge = max(1, demand / supply)
        fee = base_fare + distance * 2.0 * multiplier * surge 
        return fee

class CityStrategy:
    def calculate_fee(self, base_fare, distance, supply, demand): 
        multiplier = 1.2
        surge = max(1, demand / supply)
        fee = base_fare + distance * 1.8 * multiplier * surge 
        return fee

class SuburbsStrategy:
    def calculate_fee(self, base_fare, distance, supply, demand): 
        multiplier = 1.0
        surge = max(1, demand / supply)
        fee = base_fare + distance * 1.5 * multiplier * surge 
        return fee

class DynamicPricingModel:
    def __init__(self, strategy):
        self.strategy = strategy
    def calculate_fee(self, base_fare, distance, supply, demand):
        return self.strategy.calculate_fee(base_fare, distance, supply, demand)


def select_strategy (time, traffic_status, route_location, supply, demand): # Conditions for selecting strategies
    if traffic_status == 'heavy' or (7 <= time <= 9) or (17 <= time <= 19): return RushHourStrategy()
    elif route_location == 'city':
        return CityStrategy()
    elif route_location == 'suburbs':
        return SuburbsStrategy()
    else:
        return CityStrategy() # Default to CityStrategy if no condition matches

def main():
    # Collect rider information
    base_fare = 5.0
    distance = float(input("Enter the distance of the ride in km: "))
    time = int(input("Enter the current hour (0-23): "))
    traffic_status = input("Enter the traffic status (light, moderate, heavy): ").lower() 
    route_location = input("Enter the route location (city, suburbs): ").lower()
    supply = int(input("Enter the number of available drivers in the area: ")) 
    demand = int(input("Enter the number of ride requests in the area: "))
    # Select strategy and calculate fee
    strategy = select_strategy(time, traffic_status, route_location, supply, demand) 
    pricing_model = DynamicPricingModel(strategy)
    fee = pricing_model.calculate_fee(base_fare, distance, supply, demand)
    print (f"The selected pricing strategy is: {pricing_model.strategy}") 
    print (f"The transportation fee is: ${fee:.2f}")

if __name__ == '__main__':
    main()


class TestStrategy(unittest.TestCase):
    def test_rush_hour_strategy(self):
        rush_hour = RushHourStrategy()
        self.assertEqual(rush_hour.calculate_fee(5.0, 8, 40, 50), 35.0)
        
    def test_city_strategy(self):
        city = CityStrategy()
        self.assertEqual(city.calculate_fee(5.0, 10, 50, 40), 26.599999999999998)
        
    def test_suburbs_strategy(self):
        suburbs = SuburbsStrategy()
        self.assertEqual(suburbs.calculate_fee(5.0, 8, 40, 50), 20.0)
        
    def test_dynamic_pricing_model(self):
        rush_hour = RushHourStrategy()
        city = CityStrategy()
        suburbs = SuburbsStrategy()
        dynamic_pricing_model = DynamicPricingModel(rush_hour)
        self.assertEqual(dynamic_pricing_model.calculate_fee(5.0, 10, 10, 20), 65.0)
        dynamic_pricing_model = DynamicPricingModel(city)
        self.assertEqual(dynamic_pricing_model.calculate_fee(5.0, 10, 10, 20), 48.199999999999996)
        dynamic_pricing_model = DynamicPricingModel(suburbs)
        self.assertEqual(dynamic_pricing_model.calculate_fee(5.0, 10, 10, 20), 35.0)
        
    def test_select_strategy(self):
        self.assertEqual(select_strategy(8, 'heavy', 'city', 50, 40), RushHourStrategy())
        self.assertEqual(select_strategy(10, 'light', 'city', 10, 20), CityStrategy())
        self.assertEqual(select_strategy(12, 'light', 'suburbs', 10, 20), SuburbsStrategy())
        self.assertEqual(select_strategy(5, 'HEAVY', 'unknown', 10, 20), RushHourStrategy())
