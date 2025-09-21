# backend/fastapi_app/snapshot_service.py
# Create canonical JSON and produce SHA-256 hash for snapshots.

import hashlib
import json
from datetime import datetime

def canonical_json(obj):
    # produce a canonical JSON string: sorted keys, no extra spaces
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))

def compute_sha256(text):
    h = hashlib.sha256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()

def create_snapshot(record: dict):
    """
    record: dict containing summary, chat history, metadata, timestamp optional
    returns: {'snapshot_json': <str>, 'sha256': <str>, 'timestamp': <iso>}
    """
    record = dict(record)  # shallow copy
    record.setdefault('timestamp', datetime.utcnow().isoformat() + 'Z')
    cj = canonical_json(record)
    digest = compute_sha256(cj)
    return {'snapshot_json': cj, 'sha256': digest, 'timestamp': record['timestamp']}
