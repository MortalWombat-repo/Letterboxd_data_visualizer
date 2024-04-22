import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def get_dataset_version(*args, **kwargs):
    """
    
    """
    # Extract version information
    versions = info_json.get('versions')
    if not versions:
        return None
    latest_version = max(versions, key=lambda x: x['creationDate'])

    return latest_version['versionNumber']

def download_latest_version(dataset_name):
    current_version = get_latest_dataset_version(dataset_name)
    if not current_version:
        print("Dataset not found or no versions available.")
        return

    # Check if already downloaded or if new version
    if os.path.exists(f"{dataset_name}/version_{current_version}"):
        print("Latest version already downloaded.")
    else:
        print("Downloading newest version...")
