import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'

export default function KeywordForm() {
  const [keywords, setKeywords] = useState('')
  const navigate = useNavigate()

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    const res = await axios.post('/api/search', {
      keywords: keywords.split(/\s+/),
    })
    navigate(`/result/${res.data.job_id}`)
  }

  return (
    <form onSubmit={onSubmit} className="space-x-2">
      <input
        className="border p-2"
        value={keywords}
        onChange={(e) => setKeywords(e.target.value)}
      />
      <button type="submit" className="bg-blue-500 text-white p-2">
        Search
      </button>
    </form>
  )
}
