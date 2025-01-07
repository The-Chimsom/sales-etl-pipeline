from google.cloud import storage
import io
import pandas as pd
from ETLpipeline.config import config

cloud_config = config.get_cloud_config()

def download_file(bucket_name, source_blob_name):

 try:   
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)


    blob_data = blob.download_as_bytes()
    df = pd.read_csv(io.BytesIO(blob_data))
    print(df)
    return df

 except Exception as e:
    print(f"Error extracting from GCS: {e}")
    return None
 

if __name__ == "__main__":
    bucket_name = cloud_config['bucket_name']
    source_blob_name = cloud_config["blob_name"] 
    download_file(bucket_name=bucket_name, source_blob_name=source_blob_name)