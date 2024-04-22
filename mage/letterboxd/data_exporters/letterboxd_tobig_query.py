from google.cloud import storage

def list_gcs_files(bucket_name7666666666666666666):
  """Lists all files within the specified GCS bucket optionally starting with a prefix.

  Args:
      bucket_name (str): The name of the Google Cloud Storage bucket.
      prefix (str, optional): A prefix to filter results (e.g., 'data/'). Defaults to "".

  Returns:
      list: A list of filenames within the bucket (or filtered by prefix).
  """

  # Create a storage client
  client = storage.Client()

  # Get the bucket object
  bucket = client.bucket(bucket_name)

  # List blobs with optional prefix
  blobs = list(bucket.list_blobs(prefix=prefix))

  # Extract filenames (optional, depending on your needs)
  filenames = [blob.name for blob in blobs]

  return filenames

# Example usage
bucket_name = "bucket_letterboxd_dashboard_visualizer"

filenames = list_gcs_files(bucket_name)

print("Files in bucket:")
for filename in filenames:
  print(filename)