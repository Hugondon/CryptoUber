
class User():

    def __init__(self, name, account):
        self.name = name
        self.account = account
        

    def __str__(self):
        return f"Name: {self.name.get()}\n{self.account}"
    
    def withdraw_from_account(self, amount):
        if(amount > self.account.balance_eth.get()):
            return False
        else:
            self.account.balance_eth.set(self.account.balance_eth.get() - amount)
            return True
        
    def deposit_to_account(self, amount):
        self.account.balance_eth.set(self.account.balance_eth.get() + amount)