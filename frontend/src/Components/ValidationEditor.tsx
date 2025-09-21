import React from 'react'

export default function ValidationEditor() {
  return (
    <div className="card">
      <h3>Validation Editor</h3>
      <div style={{display:'flex', gap:16}}>
        <div style={{flex:1, border:'1px solid #eee', padding:8}}>PDF Viewer (mock)</div>
        <div style={{flex:1}}>
          <div><label>Clause text</label>
            <textarea rows={6} style={{width:'100%'}} defaultValue={'Sample extracted clause...'} />
          </div>
          <div style={{marginTop:8}}>
            <button>Approve & Save</button>
            <button style={{marginLeft:8}}>Re-index</button>
          </div>
        </div>
      </div>
    </div>
  )
}
