import { Bar, Pie } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement, Tooltip, Legend)

export default function Charts({
  pos,
  neg,
  words,
}: {
  pos: number
  neg: number
  words: Record<string, number>
}) {
  const barData = {
    labels: ['Positive', 'Negative'],
    datasets: [{ data: [pos, neg], backgroundColor: ['#4ade80', '#f87171'] }],
  }
  const pieData = {
    labels: Object.keys(words),
    datasets: [{ data: Object.values(words) }],
  }
  return (
    <div className="space-y-4">
      <Bar data={barData} />
      <Pie data={pieData} />
    </div>
  )
}
