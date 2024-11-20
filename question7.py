class RideOptionsList:
    def __init__(self) -> None:
        self.ride_options = []
    def get_ride_options(self):
        self.ride_options.append("Car")
    def compose_ride_options(self):
        return self.ride_options


class RideOptionsDecorator:
    wrapee: RideOptionsList
    def __init__(self, my_wrapee:
    RideOptionsList):
        self.wrapee = my_wrapee
    def get_ride_options(self):
        self.wrapee.ride_options.append("Bike")
        self.wrapee.get_ride_options()
    def compose_ride_options(self):
        return self.wrapee.compose_ride_options()



# Test case #1
# Testing the composition of an uninitialized list
empty_list = RideOptionsList()
list_1_results = empty_list.compose_ride_options()
assert list_1_results == [], "List was not empty!"