import React from 'react'
import Upload from './components/Upload'
import Analysis from './components/Analysis'
import ValidationEditor from './components/ValidationEditor'

export default function App() {
  return (
    <div className="app">
      <header className="topbar">
        <div className="logo">ClauseShield</div>
        <div className="actions">Demo</div>
      </header>
      <main className="main-grid">
        <aside className="sidebar">
          <nav>
            <ul>
              <li>Home</li>
              <li>Upload</li>
              <li>Dashboard</li>
              <li>Validation</li>
            </ul>
          </nav>
        </aside>
        <section className="content">
          <Upload />
          <Analysis />
          <ValidationEditor />
        </section>
      </main>
    </div>
  )
}
