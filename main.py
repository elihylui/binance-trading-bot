import json
import os
import binance_connect

import_path = "settings.json"

# Import settings
def get_settings(import_path):
    if os.path.exists(import_path):
        file = open(import_path, "r")
        project_settings = json.load(file)
        file.close()
        return project_settings
    else:
        return ImportError

if __name__ == "__main__":
    project_settings = get_settings(import_path)

    api_key = project_settings["BinanceKeys"]["API_KEY"]
    api_secret = project_settings["BinanceKeys"]["API_SECRET"]

    account = binance_connect.query_account(api_key, api_secret)
    print(account)

    status = binance_connect.query_binance_status()
    print(status)

    testnet = binance_connect.query_testnet()
