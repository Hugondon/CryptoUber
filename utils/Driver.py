class Driver():

    def __init__(self, selected, name, date, destination, number_of_seats, cost_MXN):
        self.selected = selected
        self.name = name
        self.date = date
        self.destination = destination
        self.number_of_seats = number_of_seats
        self.cost_MXN = cost_MXN

    def __str__(self):
        return f"Selected: {self.selected}\nName: {self.name}\nDate: {self.date}\nDestination: {self.destination}\nAvailable Seats: {self.number_of_seats}\nCost MXN: {self.cost_MXN}\n"
