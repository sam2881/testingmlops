import pickle
from google.cloud import storage
# from common import read_config
import os
from config.core import  GCP_BUCKET_MODEL

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/mlflowdemo-763e984441b2.json'
sec = os.environ['sec']
runid = "046015f2d1e6468c93cb90d5c789cb90"
run = "1"

cp_bucket_name = "mlflowdemoproject"
cp_blob_name = f"artifacts/{run}/{runid}/artifacts/model/model.pkl"
cp_destination_bucket_name = "mlflowdemoproject_testenvironment"
cp_destination_blob_name = f"artifacts/{run}/{runid}/artifacts/model/model.pkl"

ld_bucket_name = "mlflowdemoproject_testenvironment"
ld_model_type = "artifacts"
ld_model_filename = f"{run}/{runid}/artifacts/model/{runid}.pkl"
ld_name = f"{runid}.pkl"


dir = GCP_BUCKET_MODEL
print(dir)

for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))


def copy_blob(bucket_name, blob_name, destination_bucket_name, destination_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # destination_bucket_name = "destination-bucket-name"
    # destination_blob_name = "destination-object-name"

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


copy_blob(bucket_name=cp_bucket_name, blob_name=cp_blob_name, destination_bucket_name=cp_destination_bucket_name,
          destination_blob_name=cp_destination_blob_name)


def load_model(bucket_name, model_type, model_filename):
    try:
        storage_client = storage.Client()  # if running on GCP
        bucket = storage_client.bucket(bucket_name)
        blob1 = bucket.blob('{}/{}'.format(model_type, model_filename))
        blob1.download_to_filename('model/' + str(ld_name))
        return True, None
    except Exception as e:
        print('Something went wrong when trying to load previous model from GCS bucket. Exception: ' + str(e),
              flush=True)
        return False, e


load_model(ld_bucket_name, ld_model_type, ld_model_filename)


def cour():
    pass
