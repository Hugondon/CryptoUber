class CryptoAccount():

    def __init__(self, id, balance_eth, public_key):
        self.id = id
        self.balance_eth = balance_eth
        self.public_key = public_key

    def __str__(self):
        return f"Account ID: {self.id}\nAccount Balance: {self.balance_eth.get()}\nAccount Public Key: {self.public_key}\n"
