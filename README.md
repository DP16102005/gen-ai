ClauseShield - POC Code Bundle
------------------------------
This bundle contains a minimal prototype scaffold (backend + frontend skeleton + scripts)
for the ClauseShield hackathon POC. Edit cloud integrations and credentials before production use.
## Next steps (integrate with Google Cloud)
1. Create GCP project and enable APIs: Cloud Run, Cloud Storage, Pub/Sub, Vertex AI, Firestore, Cloud Build.
2. Create a GCS bucket and set GCS_BUCKET in .env
3. Install Google Cloud SDK locally and authenticate `gcloud auth login`
4. For embeddings & LLM: install Vertex AI SDK and follow Vertex docs to enable models.
5. Update `vertex_client.py` to call real Vertex AI embedding & generation APIs.
6. Deploy backend to Cloud Run via Cloud Build (use cloudbuild.yaml).
