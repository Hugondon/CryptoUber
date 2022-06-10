from utils.Driver import Driver
from utils.CryptoAccount import CryptoAccount

EXAMPLE_ACCOUNT_1 = CryptoAccount(
    id="0x0FaD3a9623A8841C2B43340CD9415f9daa8F8eE1",
    balance_eth=50,
    public_key="a209458ce6cbc3f1326ffd9fb8c0e0f1073ae1946c9b0e4b0b00b7d901db7f0c"
) 
EXAMPLE_ACCOUNT_2 = CryptoAccount(
    id="0x7068437B8D37DD9376cB261f32dF6016bBCd0e47",
    balance_eth=100,
    public_key="06d342fd7ead263c2f5211845a9e3866eab481e320b9decf794f91f0745a0fe0"
)
EXAMPLE_ACCOUNT_3 = CryptoAccount(
    id="0x1C561aA1185d5A8bd31720F63FFE883e96E16765",
    balance_eth=150,
    public_key="7429f1673fc93c5135ae826822944bdc0b14ce76afffe0dd5df9e3ee6e49897b"
)
EXAMPLE_ACCOUNT_4 = CryptoAccount(
    id="0xFE9BC9391c9dE7bFcE93cC62244766f43E3f630C",
    balance_eth=200,
    public_key="fcbcaa605bc0cf2e4fed0d47f3e272df3ef6e04b2f1250e213358d9715760889"
)

EXAMPLE_DRIVER_1 = Driver(selected=False, name="David", date="10:00 - 15:30",
                          destination="Edif. Sur", number_of_seats=2, cost_MXN=50, timeout_s=10,
                          account=EXAMPLE_ACCOUNT_1)
EXAMPLE_DRIVER_2 = Driver(selected=False, name="Alex", date="10:00 - 15:45",
                          destination="Disney", number_of_seats=2, cost_MXN=60, timeout_s=20,
                          account=EXAMPLE_ACCOUNT_2)
EXAMPLE_DRIVER_3 = Driver(selected=False, name="Luis", date="10:00 - 17:00",
                          destination="CIEE", number_of_seats=3, cost_MXN=50, timeout_s=30,
                          account=EXAMPLE_ACCOUNT_3)
EXAMPLE_DRIVER_4 = Driver(selected=False, name="Andy", date="10:00 - 16:00",
                          destination="Edif. Sur", number_of_seats=1, cost_MXN=45, timeout_s=40,
                          account=EXAMPLE_ACCOUNT_4)
