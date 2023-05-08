import json
import os
import binance

import_path="settings.json"

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
    secret_key = project_settings["BinanceKeys"]["SECRET_KEY"]

