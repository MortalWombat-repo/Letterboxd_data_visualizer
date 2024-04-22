from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import inflect

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(destination_directory: str) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    print(destination_directory)

    # Iterate over each file in the directory
    for num, filename in enumerate(os.listdir(destination_directory), start=1):
        # Combine directory path and filename to get full path
        full_path = os.path.join(destination_directory, filename)
    
        # Read the file
        data = pd.read_csv(full_path, compression='zip')
        #print(data)

        # Export to Parquet format
        parquet_filename = os.path.splitext(filename)[0].replace(".csv", "") + '_uncleaned'
        
        pq.write_table(pa.Table.from_pandas(data), parquet_filename)
        #print(parquet_filename)
        print(f"{num}. {filename} (full path: {full_path})")

        # Check if the Parquet file was successfully created
        p = inflect.engine()
        if os.path.exists(parquet_filename):
            print(f"{p.ordinal(num)}. Parquet file created successfully. -> {parquet_filename}")
        else:
            print(f"Error: {p.ordinal(num)}. Parquet file creation failed.")

        # Upload Parquet file to Google Cloud Storage
        config_path = path.join(get_repo_path(), 'io_config.yaml')
        config_profile = 'default'

        bucket_name = 'bucket_letterboxd_dashboard_visualizer'
        object_key = parquet_filename

        GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
            parquet_filename,
            bucket_name,
            object_key + '.parquet',
            format = 'parquet'
        )

    print(f"Exporting {num} files to a Google Storage bucket.")
