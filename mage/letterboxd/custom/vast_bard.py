if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    import subprocess
    import os
    import json
    import shutil
    from kaggle.api.kaggle_api_extended import KaggleApi

    try:
        import requests
        import pandas as pd
        import kaggle
        from google.oauth2.service_account import Credentials
        from google.cloud import storage
    except ImportError:
        print("Some packages are missing. Installing necessary packages...")
        subprocess.check_call(["pip", "install", "kaggle", "requests", "pandas", "google-auth", "google-cloud-storage"])
        import requests
        import pandas as pd
        import kaggle
        from google.oauth2.service_account import Credentials
        from google.cloud import storage

    # Load Kaggle API credentials from JSON file
    credentials_file = "/home/src/keys/kaggle.json" # Update with the path to your JSON file
    with open(credentials_file, "r") as f:
        kaggle_credentials = json.load(f)

    # Set Kaggle API credentials as environment variables
    os.environ['KAGGLE_USERNAME'] = kaggle_credentials['username']
    os.environ['KAGGLE_KEY'] = kaggle_credentials['key']

    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()

    # download single file
    #Signature: dataset_download_file(dataset, file_name, path=None, force=False, quiet=True)
    api.dataset_download_file('gsimonx37/letterboxd','genres.csv')

    current_working_directory = os.getcwd()

    # Print the current working directory
    print(current_working_directory)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
