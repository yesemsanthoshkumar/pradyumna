"""
Reads configuration settings from config.json and
make it available over the application
"""

import json

CONFIG = None
with open("config.json", 'r') as cfg:
    CONFIG = json.load(cfg)

print(CONFIG)
