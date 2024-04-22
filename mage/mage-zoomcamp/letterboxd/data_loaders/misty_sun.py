import io
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
    
    # Set the configuration for the Kaggle API
    api = KaggleApi()
    try:
        api.authenticate()
        print("Kaggle API authentication successful")
    except Exception as e:
        print("Error authenticating Kaggle API:", str(e))
    
    # Define the destination directory where you want to save the downloaded file
    destination_directory = "/home/src/project/kaggle"  # Update with your desired directory
    try:
        os.makedirs(destination_directory, exist_ok=True)
        print("Destination directory exists or created successfully")
    except Exception as e:
        print("Error creating destination directory:", str(e))
    return api

@test
def test_output(api) -> None:
    """
    Template code for testing the output of the block.
    """
    assert api is not None, 'The output is undefined'