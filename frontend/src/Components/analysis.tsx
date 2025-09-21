import React, { useState } from 'react'
import axios from 'axios'

export default function Analysis() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState<any>(null)

  async function ask() {
    try {
      const resp = await axios.post('/api/analyze', { question })
      setAnswer(resp.data)
    } catch (err) {
      setAnswer({ answer: 'Error' })
    }
  }

  return (
    <div className="card">
      <h3>Analysis</h3>
      <input value={question} onChange={e => setQuestion(e.target.value)} placeholder="Ask about the contract..." />
      <button onClick={ask}>Ask</button>
      <pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(answer, null, 2)}</pre>
    </div>
  )
}
