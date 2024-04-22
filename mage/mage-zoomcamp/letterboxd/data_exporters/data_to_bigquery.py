from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow.fs import GcsFileSystem

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

from google.cloud import storage

#if 'custom' not in globals():
    #from mage_ai.data_preparation.decorators import custom

@data_exporter
def export_data_to_big_query(*args, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    #Lists all the blobs in the bucket.
    project_name = "letterboxd_visualizer"
    dataset = "letterboxd_data"
    bucket_name = "bucket_letterboxd_dashboard_visualizer"
    storage_client = storage.Client()
    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)
    # Note: The call returns a response only when the iterator is consumed.
    parquet_files = []
    for blob in blobs:
        print(blob.name)
        parquet_files.append(blob.name)
    print(parquet_files)

    for table in parquet_files:
        name = table.replace("_uncleaned.parquet", "")
        print(table.replace("_uncleaned.parquet", ""))

        bucket_name = bucket_name
        blob_prefix = table
        root_path = f"{bucket_name}/{blob_prefix}"    
        pa_table = pq.read_table(
            source=root_path,
            filesystem=GcsFileSystem(),
        )
        print(pa_table)
    