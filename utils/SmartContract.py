class SmartContract():

    def __init__(self, driver, destination, start_travel_time, number_of_seats, duration, cost_eth, expiration_time_s):
        self.driver = driver
        self.destination = destination
        self.start_travel_time = start_travel_time
        self.number_of_seats = number_of_seats
        self.duration = duration
        self.cost_eth = cost_eth
        self.expiration_time_s = expiration_time_s 

    def __str__(self):
        return f"Smart Contract\nDriver: {self.driver}\nDestination: {self.destination}\nStart Travel Time: {self.start_travel_time}\nDuration: {self.duration}\nCost: {self.cost_eth}\nExpiration Time: {self.expiration_time_s}\n"
