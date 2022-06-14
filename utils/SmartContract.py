from solcx import compile_source

class SmartContract():

    def __init__(self, driver, destination, start_travel_time, number_of_seats, duration, cost_eth, expiration_time_s):
        self.driver = driver
        self.destination = destination
        self.start_travel_time = start_travel_time
        self.number_of_seats = number_of_seats
        self.duration = duration
        self.cost_eth = cost_eth
        self.expiration_time_s = expiration_time_s
        
        source_code = f'''
        pragma solidity >0.5.0;

            contract Greeter {{
                string public driver;
                string public destination;
                string public startTravelTime;
                uint public maxNumberOfSeats;
                uint public duration;
                uint public expirationTime;

                constructor() public {{
                    driver = "{self.driver}";
                    destination = "{self.destination}";
                    startTravelTime = "{self.start_travel_time}";
                    maxNumberOfSeats = {self.number_of_seats};
                    duration = {self.duration};
                    expirationTime = {self.expiration_time_s};
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
                function getmaxNumberOfSeats() view public returns (uint) {{
                    return maxNumberOfSeats;
                }}
                function getDuration() view public returns (uint) {{
                    return duration;
                }}
                function getExpirationTime() view public returns (uint) {{
                    return expirationTime;
                }}
        }}
        '''

        # Solidity source code
        compiled_solidity = compile_source(
            source_code,
            output_values=['abi', 'bin']
        ) 
        
        contract_id, contract_interface = compiled_solidity.popitem()
        self.bytecode, self.abi = contract_interface['bin'], contract_interface['abi']

    def __str__(self):
        return f"Smart Contract\nDriver: {self.driver}\nDestination: {self.destination}\nStart Travel Time: {self.start_travel_time}\nDuration: {self.duration}\nCost: {self.cost_eth}\nExpiration Time: {self.expiration_time_s}\n"
