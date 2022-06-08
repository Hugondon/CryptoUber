from web3 import Web3
from solcx import compile_source


driver_name = 'Hugo'
duration = 30
start_travel_hour = 14
start_travel_minute = 30

source_string = f'''
pragma solidity >0.5.0;

contract Greeter {{
string public driver;
string public start_travel_time;
uint public duration;


constructor() public {{
    driver = {driver_name};
    duration = {duration};
    startTravelTime = {start_travel_hour}:{start_travel_minute};
}}

function setGreeting(string memory _greeting) public {{
    driver = _greeting;
}}

function getDriver() view public returns (uint duration1) {{
    return driver;
}}
function getDuration() view public returns (uint duration2) {{
    return duration;
}}
function getStartTravelTime() view public returns (uint duration2) {{
    return startTravelTime;
}}
}}
'''

compiled_sol = compile_source(
source_string,
output_values=['abi', 'bin']
)

contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
web3.eth.defaultAccount=web3.eth.accounts[0]

# web3.py instance
#w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
#w3.eth.default_account = w3.eth.accounts[0]

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()
print(web3.toHex(tx_hash))

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

greeter = web3.eth.contract(
     address=tx_receipt.contractAddress,
     abi=abi
 )

print(greeter.functions.greet().call())
print(greeter.functions.duration1().call())
print(greeter.functions.contract1().call())
print(greeter.functions.startTravel1().call())
 
# tx_hash = greeter.functions.setGreeting('Nihao').transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
# print(greeter.functions.greet().call())