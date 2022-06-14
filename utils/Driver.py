class Driver():

    def __init__(self, selected, name, account, contract):
        self.selected = selected
        self.name = name
        self.account = account
        self.current_contract = contract
        self.contracts = []
    
    def __str__(self):
        return f"Selected: {self.selected}\nName: {self.name}\nDate: {self.date}\nDestination: {self.destination}\nAvailable Seats: {self.number_of_seats}\nCost MXN: {self.cost_MXN}\n"
