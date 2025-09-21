# backend/fastapi_app/vertex_client.py
# Template: Vertex AI embedding & LLM client calls.
# Requires google-cloud-aiplatform or vertex-ai SDK. This is a minimal template.

import os
# from google.cloud import aiplatform  # Uncomment when SDK installed
# from vertexai import language_models  # If using vertexai SDK

PROJECT = os.environ.get("GCP_PROJECT")
LOCATION = os.environ.get("GCP_LOCATION", "us-central1")
EMBEDDING_MODEL = os.environ.get("VERTEX_EMBEDDING_MODEL", "textembedding-gecko")  # placeholder
LLM_MODEL = os.environ.get("VERTEX_LLM_MODEL", "text-bison")  # placeholder

def embed_texts(texts):
    """
    Return list of embeddings matching order of texts.
    Replace with real Vertex AI SDK calls.
    """
    # Example sketch using vertexai SDK (non-functional until installed and configured):
    # model = language_models.TextEmbeddingModel.from_pretrained(EMBEDDING_MODEL)
    # embeddings = model.get_embeddings(texts)
    # return [e.values for e in embeddings]
    # Placeholder: return zero vectors sized 1536
    return [[0.0] * 1536 for _ in texts]

def generate_answer(prompt, temperature=0.0, max_tokens=512):
    """
    Call Vertex LLM to generate answer from prompt. Replace with real SDK.
    """
    # Example pseudo:
    # model = language_models.TextGenerationModel.from_pretrained(LLM_MODEL)
    # response = model.generate(prompt, max_output_tokens=max_tokens, temperature=temperature)
    # return response.text
    return "DEMO ANSWER: This is a placeholder response. Replace with Vertex AI call."
