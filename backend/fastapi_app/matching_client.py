# backend/fastapi_app/matching_client.py
# Template for interacting with a vector similarity engine.
# For POC, this file contains stubs; replace with Vertex Matching Engine or Pinecone SDK.

def upsert_vectors(vectors):
    """
    vectors: list of dicts {'id': 'chunk_id', 'values': [float,...], 'metadata': {...}}
    """
    # TODO: call Vertex Matching Engine or Pinecone to upsert
    print(f"[matching_client] upsert {len(vectors)} vectors (demo)")

def query_similar(embedding, top_k=5):
    """
    Return list of matches: [{'id':..., 'score':..., 'metadata':..., 'text':...}, ...]
    """
    # TODO: query Matching Engine; here we return mocked results
    return [
        {'id': 'chunk_mock_1', 'score': 0.95, 'metadata': {'page': 2}, 'text': 'Mocked chunk text 1'},
        {'id': 'chunk_mock_2', 'score': 0.88, 'metadata': {'page': 4}, 'text': 'Mocked chunk text 2'},
    ]
