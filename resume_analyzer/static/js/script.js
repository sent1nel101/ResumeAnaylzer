function downloadRewritten() {
  const rewrittenText = document.querySelector("pre").innerText
  const blob = new Blob([rewrittenText], { type: "text/plain" })
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement("a")
  a.href = url
  a.download = "rewritten_resume.txt"
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
}
