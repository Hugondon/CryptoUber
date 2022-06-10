
from web3 import Web3
from solcx import compile_source

GANACHE_URL = 'HTTP://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(GANACHE_URL))
web3.eth.defaultAccount=web3.eth.accounts[0]

driver_name = 'Hugo'
destination = "CDT"
duration_m = 30
start_travel_hour = 14
start_travel_minute = 30

source_code = f'''
pragma solidity >0.5.0;

    contract Greeter {{
        string public driver;
        string public destination;
        string public startTravelTime;
        uint public duration;


        constructor() public {{
            driver = "{driver_name}";
            destination = "{destination}";
            startTravelTime = "{start_travel_hour}:{start_travel_minute}";
            duration = {duration_m};
        }}

        function getDriver() view public returns (string memory) {{
            return driver;
        }}
        function getDestination() view public returns (string memory) {{
            return destination;
        }}
        function getStartTravelTime() view public returns (string memory) {{
            return startTravelTime;
        }}
        function getDuration() view public returns (uint) {{
            return duration;
        }}
        
}}
'''

# Solidity source code
compiled_solidity = compile_source(
    source_code,
     output_values=['abi', 'bin']
 )

contract_id, contract_interface = compiled_solidity.popitem()
bytecode, abi = contract_interface['bin'], contract_interface['abi']

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()
print(f"Hash: {web3.toHex(tx_hash)}")

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Contact Address: {tx_receipt.contractAddress}")

greeter = web3.eth.contract(
     address=tx_receipt.contractAddress,
     abi=abi
 )

# print(f"Driver Name: {greeter.functions.getDriver().call()}")
# print(f"Destination: {greeter.functions.getDestination().call()}")
# print(f"Duration: {greeter.functions.getDuration().call()} minutes")
# print(f"Starting Travel Time: {greeter.functions.getStartTravelTime().call()}")

# Esto debe ir en donde se acepte la transaccion
        # self.Greeter = self.parent.web3.eth.contract(abi=abi, bytecode=bytecode)
        
        # # Submit the transaction that deploys the contract
        # tx_hash = self.Greeter.constructor().transact()
        # print(self.parent.web3.toHex(tx_hash))      
        # tx_receipt = self.parent.web3.eth.wait_for_transaction_receipt(tx_hash)
        
        # self.greeter = self.parent.web3.eth.contract(
        #     address=tx_receipt.contractAddress,
        #     abi=abi
        # )
        
        # print(self.greeter.functions.getDriver().call())
        # print(self.greeter.functions.getDuration().call())
        # print(self.greeter.functions.getStartTravelTime().call())
        
        # tx_receipt = self.parent.web3.eth.wait_for_transaction_receipt(tx_hash)