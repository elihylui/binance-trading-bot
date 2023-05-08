from binance.spot import Spot
import pandas

# Function to get the status
def query_binance_status():
    status = Spot().system_status()
    if status['status'] == 0:
        return True
    else:
        raise ConnectionError

# Function to query account
def query_account(api_key, api_secret):
    return Spot(
        api_key = api_key,
        api_secret = api_secret,
        base_url = 'https://testnet.binance.vision',
    ).account()

# Function to query testnet
def query_testnet():
    client = Spot(base_url='https://testnet.binance.vision')
    print(client.time())


