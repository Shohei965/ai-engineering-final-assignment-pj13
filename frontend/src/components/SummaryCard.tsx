export default function SummaryCard({ summary }: { summary: string }) {
  return (
    <div className="border p-4 shadow">
      <p>{summary}</p>
    </div>
  )
}
