import io
import subprocess
import pandas as pd
import os
import requests
from zipfile import ZipFile
import json
from kaggle.api.kaggle_api_extended import KaggleApi


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

#1st step add project in the form "user/project_name"
project = "gsimonx37/letterboxd"
# Update with your desired directory
destination_directory = "/home/src/project/kaggle" 

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    List all subfiles you need
    """
    '''
    dataset_files = [

        (project, "actors.csv"),
        (project, "countries.csv"),
        (project, "crew.csv"),
        (project, "genres.csv"),
        (project, "languages.csv"),
        (project, "movies.csv"),
        (project, "releases.csv"),
        (project, "studios.csv"),
        (project, "themes.csv")
        
    ]
    '''
    dataset_files = [

        (project, "genres.csv"),
        (project, "themes.csv")
    ]

    #create .kaggle folder
    # Define the directory path
    kaggle_dir = os.path.expanduser("~/.kaggle")

    # Check if the directory exists
    if os.path.exists(kaggle_dir):
        print(f"The directory '{kaggle_dir}' already exists.")
    else:
        # Create the directory using the mkdir command
        subprocess.run(f"mkdir -p {kaggle_dir}", shell=True)
        print(f"The directory '{kaggle_dir}' has been created.")

    # Import Kaggle credentials
    credentials_file = "/home/src/keys/kaggle.json"  # Update with the path to your JSON file
    #copy the credentials to kaggle dir
    copy_kaggle_auth = f"cp {credentials_file} /root/.kaggle/kaggle.json"
    subprocess.run(copy_kaggle_auth, shell=True)
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
    
    # Define the destination directory where you want to save the downloaded file
    if os.path.exists(destination_directory):
        print(f"The directory '{destination_directory}' already exists.")
    else:
        # Create the directory using the mkdir command
        subprocess.run(f"mkdir -p {destination_directory}", shell=True)
        print(f"The directory '{destination_directory}' has been created.")

    data_file_paths = []  # List to store downloaded data paths
    # Download and unzip each file
    for dataset, file_name in dataset_files:
        print(dataset, file_name)
        # Download the file
        #command = f"kaggle datasets download {dataset} -f {file_name} -p {destination_directory}"
        #subprocess.run(command, shell=True)
   
        # Download and unzip each file

        # Construct the downloaded data path
        data_file_path = os.path.join(destination_directory, file_name)
        data_file_paths.append(data_file_path)
        
        '''
        #Pandas can read zipped files. To save space they are 
        zipped at a neglible efficiency loss for the data size.
        # Unzip the downloaded file

        zip_file_path = os.path.join(destination_directory, f"{file_name}.zip")
        with ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_directory)
        
        # Remove the zip file after extraction
        os.remove(zip_file_path)
        '''

    # Print confirmation
    print("Files downloaded and extracted successfully!")

    return destination_directory