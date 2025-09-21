# backend/fastapi_app/gcs_signed_url.py
# Lightweight helper to create signed upload URLs for Google Cloud Storage.
# Requires `google-cloud-storage` package and GCP credentials (service account).

from google.cloud import storage
from datetime import timedelta
import os

GCP_PROJECT = os.environ.get("GCP_PROJECT")
GCS_BUCKET = os.environ.get("GCS_BUCKET", "clauseshield-uploads")

def generate_signed_upload_url(filename: str, content_type: str = "application/pdf", expires_minutes: int = 15):
    client = storage.Client(project=GCP_PROJECT)
    bucket = client.bucket(GCS_BUCKET)
    blob = bucket.blob(filename)
    url = blob.generate_signed_url(
        version="v4",
        expiration=timedelta(minutes=expires_minutes),
        method="PUT",
        content_type=content_type,
    )
    return url
