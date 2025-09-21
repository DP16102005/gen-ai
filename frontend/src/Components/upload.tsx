import React, { useState } from 'react'
import axios from 'axios'

export default function Upload() {
  const [file, setFile] = useState<File | null>(null)
  const [status, setStatus] = useState('')

  async function handleUpload() {
    if (!file) return
    setStatus('Uploading...')
    const form = new FormData()
    form.append('file', file)
    try {
      const resp = await axios.post('/api/upload', form, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      setStatus('Uploaded: ' + resp.data.filename)
    } catch (err) {
      setStatus('Upload failed')
    }
  }

  return (
    <div className="card">
      <h3>Upload Contract</h3>
      <input type="file" accept="application/pdf" onChange={e => setFile(e.target.files?.[0] ?? null)} />
      <button onClick={handleUpload}>Upload PDF</button>
      <div>{status}</div>
    </div>
  )
}
