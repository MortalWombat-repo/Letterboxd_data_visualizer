from google.cloud import storage

#if 'custom' not in globals():
    #from mage_ai.data_preparation.decorators import custom

#@custom
def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"
    storage_client = storage.Client()
    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)
    # Note: The call returns a response only when the iterator is consumed.
    parquet_files = []
    for blob in blobs:
        print(blob.name)
        parquet_files.append(blob.name)
    print(parquet_files)
    return parquet_files

list_blobs("bucket_letterboxd_dashboard_visualizer")
