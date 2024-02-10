import json
import os

class Helper:
    def __init__(self):
        pass

    def load_config(self, configPath = "./config.json"):

        # Load the JSON config file
        with open(configPath, 'r') as file:
            config = json.load(file)

        # Set environment variables
        for key, value in config.items():
            os.environ[key.upper()] = str(value)

        print("Environment variables set.")