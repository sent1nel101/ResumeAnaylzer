function downloadRewritten(format = 'txt') {
  const rewrittenText = document.querySelector("pre").innerText
  
  if (format === 'txt') {
    // Direct download for TXT
    const blob = new Blob([rewrittenText], { type: "text/plain" })
    const url = window.URL.createObjectURL(blob)
    const a = document.createElement("a")
    a.href = url
    a.download = "rewritten_resume.txt"
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    window.URL.revokeObjectURL(url)
  } else {
    // Server-side generation for PDF and DOCX
    const form = document.createElement('form')
    form.method = 'POST'
    form.action = `/download/${format}`
    form.style.display = 'none'
    
    const textInput = document.createElement('input')
    textInput.type = 'hidden'
    textInput.name = 'resume_text'
    textInput.value = rewrittenText
    
    form.appendChild(textInput)
    document.body.appendChild(form)
    form.submit()
    document.body.removeChild(form)
  }
}

// File upload feedback functionality
document.addEventListener('DOMContentLoaded', function() {
  const fileInput = document.getElementById('resume-file');
  const uploadIcon = document.querySelector('.upload-icon');
  const uploadText = document.querySelector('.upload-text');
  
  if (fileInput) {
    fileInput.addEventListener('change', function() {
      if (this.files && this.files.length > 0) {
        const fileName = this.files[0].name;
        uploadIcon.textContent = '✅';
        uploadText.textContent = `Selected: ${fileName}`;
        uploadText.parentElement.style.color = '#4caf50';
      } else {
        uploadIcon.textContent = '📄';
        uploadText.textContent = 'Choose Resume File';
        uploadText.parentElement.style.color = '';
      }
    });
  }
});
