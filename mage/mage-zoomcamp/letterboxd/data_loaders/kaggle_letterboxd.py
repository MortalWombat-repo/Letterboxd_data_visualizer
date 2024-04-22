import os
import json
import pandas as pd
import subprocess
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi

# Import Kaggle credentials
credentials_file = "/home/src/keys/kaggle.json"  # Update with the path to your JSON file
with open(credentials_file, "r") as f:
    kaggle_credentials = json.load(f)

# Set the configuration for the Kaggle API
api = KaggleApi()
api.authenticate()

# Define the destination directory where you want to save the downloaded file
destination_directory = "/home/src/"  # Update with your desired directory

# Define the Kaggle dataset names and file names
datasets_files = [
    ("gsimonx37/letterboxd", "genres.csv"),
    ("gsimonx37/letterboxd", "themes.csv"),
    ("gsimonx37/letterboxd", "movies.csv")
]

# Download and unzip each file
for dataset, file_name in datasets_files:
    # Download the file
    command = f"kaggle datasets download {dataset} -f {file_name} -p {destination_directory}"
    subprocess.run(command, shell=True)
    
    # Unzip the downloaded file
    zip_file_path = os.path.join(destination_directory, f"{file_name}.zip")
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)
    
    # Remove the zip file after extraction
    os.remove(zip_file_path)

# Load the genres CSV file into a DataFrame
genres_csv_file = os.path.join(destination_directory, 'genres.csv')
data = pd.read_csv(genres_csv_file)

# Display the first few rows of the DataFrame
print(data.head())

# Print confirmation
print("Files downloaded and extracted successfully!")