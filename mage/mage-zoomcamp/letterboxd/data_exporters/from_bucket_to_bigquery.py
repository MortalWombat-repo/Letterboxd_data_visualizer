from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

import pyarrow.parquet as pq
from pyarrow.fs import GcsFileSystem

@data_loader
def load_data(*args, **kwargs):
    bucket_name = 'bucket_letterboxd_dashboard_visualizer'
    blob_prefix = '/*.parquet'
    root_path = f"gs://{bucket_name}/{blob_prefix}"
    
    gcs = GcsFileSystem()
    files = gcs.get_file_info(root_path).file_name
    
    dfs = []
    for file in files:
        file_path = f"{root_path}/{file}"
        table = pq.read_table(file_path, filesystem=gcs).to_pandas()
        dfs.append(table)
    
    return pd.concat(dfs)