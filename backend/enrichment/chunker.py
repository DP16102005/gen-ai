import re, uuid
def paragraph_split(text):
    return [p.strip() for p in text.split('\n\n') if p.strip()]
def sentence_split(paragraph):
    return re.split(r'(?<=[.!?])\s+', paragraph)
def chunk_text(text, chunk_size=800, overlap=200):
    paragraphs = paragraph_split(text)
    chunks = []
    for para in paragraphs:
        sentences = sentence_split(para)
        cur = ''
        for s in sentences:
            if len(cur) + len(s) + 1 <= chunk_size:
                cur = (cur + ' ' + s).strip()
            else:
                if cur:
                    chunks.append({'chunk_id': f'chunk_{uuid.uuid4().hex[:8]}','page': None,'text': cur,'source': None})
                cur = s.strip()
        if cur:
            chunks.append({'chunk_id': f'chunk_{uuid.uuid4().hex[:8]}','page': None,'text': cur,'source': None})
    return chunks[:500]
