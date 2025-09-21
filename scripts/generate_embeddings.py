import json, sys
def load_chunks(path):
    with open(path,'r',encoding='utf-8') as f:
        return json.load(f)
def fake_embed(text):
    return [float(ord(c) % 10) for c in text[:128]]
def main(chunks_path):
    chunks = load_chunks(chunks_path)
    vectors = []
    for c in chunks:
        v = fake_embed(c.get('text',''))
        vectors.append({'id': c['chunk_id'], 'values': v, 'metadata': {'page': c.get('page')}})
    print('Prepared', len(vectors), 'vectors (demo)')
if __name__=='__main__':
    if len(sys.argv)<2:
        print('Usage: python generate_embeddings.py <chunks.json>')
    else:
        main(sys.argv[1])
