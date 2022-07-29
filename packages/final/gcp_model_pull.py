import pickle
import yaml
from google.cloud import storage

import os
import typing as t
# from final.config.core import config
from pathlib import Path
mlflow_id = "7f75e29729e249b088d55bef81550402"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/mlops-353417-0d6234ccd6b9.json'
bucket_name = "mlops_artifacts_1"
model_type = "artifacts"
model_filename = f"0/{mlflow_id}/artifacts/model/{mlflow_id}.pkl"

from pathlib import Path

# PACKAGE_ROOT = Path(packages.__file__).resolve().parent
# TRAINED_MODEL_DIR = "packages/final/model/"
name = f"{mlflow_id}.pkl"
#
dir = r'C:\Users\Samrat\Desktop\testingmlops\packages\final\model'


for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))


def load_model(bucket_name, model_type, model_filename):

    try:
        storage_client = storage.Client()  # if running on GCP
        bucket = storage_client.bucket(bucket_name)
        blob1 = bucket.blob('{}/{}'.format(model_type, model_filename))
        blob1.download_to_filename('model/' + str(name))
        return True, None
    except Exception as e:
        print('Something went wrong when trying to load previous model from GCS bucket. Exception: ' + str(e),
              flush=True)
        return False, e


load_model(bucket_name, model_type, model_filename)
