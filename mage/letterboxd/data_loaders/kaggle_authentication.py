import io
import subprocess
import pandas as pd
import os
import requests
import json
from kaggle.api.kaggle_api_extended import KaggleApi

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def connect_api(*args, **kwargs):
    # Import Kaggle credentials
    credentials_file = "/home/src/keys/kaggle.json"  # Update with the path to your JSON file
    with open(credentials_file, "r") as f:
        kaggle_credentials = json.load(f)
    #adding chmod 600 so only the owner can edit
    file_permissions = "chmod 600 /root/.kaggle/kaggle.json"
    subprocess.run(file_permissions, shell=True)
    
    # Set the configuration for the Kaggle API
    api = KaggleApi()
    try:
        api.authenticate()
        print("Kaggle API authentication successful")
    except Exception as e:
        print("Error authenticating Kaggle API:", str(e))