from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid, json, pathlib
from ..enrichment.chunker import chunk_text

app = FastAPI(title='ClauseShield POC - ML Service')
STORAGE_DIR = pathlib.Path(__file__).resolve().parent.parent / 'storage'
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

class AnalyzeRequest(BaseModel):
    question: str

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    dest = STORAGE_DIR / f"{uuid.uuid4().hex}_{file.filename}"
    with open(dest, 'wb') as f:
        f.write(await file.read())
    return {'filename': dest.name, 'size': dest.stat().st_size}

@app.post('/process_document')
async def process_document(filename: str):
    path = STORAGE_DIR / filename
    if not path.exists():
        raise HTTPException(status_code=404, detail='file not found')
    text = path.read_text(encoding='utf-8', errors='ignore')
    chunks = chunk_text(text, chunk_size=800, overlap=200)
    out = path.with_suffix('.chunks.json')
    out.write_text(json.dumps(chunks, indent=2), encoding='utf-8')
    return {'chunks_file': out.name, 'num_chunks': len(chunks)}

@app.post('/analyze')
async def analyze(req: AnalyzeRequest):
    answer = {
        'answer': 'Mocked: The termination clause states 30 days notice. (demo)',
        'sources': [
            {'page': 4, 'chunk_id': 'chunk_0003', 'text': '...termination clause text...', 'confidence': 0.87}
        ]
    }
    return JSONResponse(content=answer)
