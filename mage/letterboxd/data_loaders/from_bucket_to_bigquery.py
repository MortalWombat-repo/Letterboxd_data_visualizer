from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pyarrow.parquet as pq
from pyarrow.fs import GcsFileSystem
from google.cloud import storage

@data_loader
def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    all_files = []
    for blob in blobs:
        print(blob.name)
        all_files.append(blob.name)

    return all_files

# Replace 'your-bucket-name' with the name of your bucket
list_blobs('bucket_letterboxd_dashboard_visualizer')
    
    