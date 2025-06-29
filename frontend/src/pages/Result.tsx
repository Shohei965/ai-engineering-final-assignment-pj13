import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'

import SummaryCard from '../components/SummaryCard'
import Charts from '../components/Charts'

type ResultData = {
  summary: string
  pos_count: number
  neg_count: number
  word_freq: Record<string, number>
  samples: any[]
}

export default function Result() {
  const { jobId } = useParams<{ jobId: string }>()
  const [data, setData] = useState<ResultData | null>(null)

  useEffect(() => {
    const interval = setInterval(async () => {

      if (res.data.summary) {
        setData(res.data)
        clearInterval(interval)
      }
    }, 1000)
    return () => clearInterval(interval)
  }, [jobId])

  if (!data) return <div>Loading...</div>

  return (
    <div className="p-4 space-y-4">
      <SummaryCard summary={data.summary} />
      <Charts pos={data.pos_count} neg={data.neg_count} words={data.word_freq} />
      <div className="mt-4">
        {data.samples.map((s, i) => (
          <p key={i}>{JSON.stringify(s)}</p>
        ))}
      </div>
    </div>
  )
}
