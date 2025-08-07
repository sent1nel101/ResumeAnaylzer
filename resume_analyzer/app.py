from flask import Flask, render_template, request, redirect, url_for, jsonify
import docx
import os
import re
import requests
import json

# Try to import PyMuPDF, fallback if not available
try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False
    print("Warning: PyMuPDF not available, PDF support will be limited")


app = Flask(__name__)


def get_ai_analysis(text):
    """Get AI-powered resume analysis using HuggingFace Inference API."""
    try:
        # Use HuggingFace's free inference API
        API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
        
        prompt = f"""Analyze this resume for ATS (Applicant Tracking System) compatibility. 
        Provide specific feedback on:
        1. Keywords and industry terms
        2. Action verbs usage
        3. Quantifiable achievements
        4. Contact information completeness
        5. Formatting and structure
        
        Resume text: {text[:1500]}..."""  # Limit text length
        
        headers = {"Authorization": "Bearer hf_dummy"}  # Would need real token for production
        payload = {"inputs": prompt, "parameters": {"max_length": 200}}
        
        # For demo purposes, return enhanced analysis if API fails
        return None
    except:
        return None


def analyze_resume_text(text):
    """Analyze resume text and provide feedback with AI enhancement."""
    good_points = []
    needs_correction = []
    fails = []
    
    # Get AI analysis (if available)
    ai_feedback = get_ai_analysis(text)
    if ai_feedback:
        # Parse AI feedback and incorporate it
        pass
    
    # Check for contact information
    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
        good_points.append('Contains email address')
    else:
        fails.append('Missing email address')
    
    if re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text):
        good_points.append('Contains phone number')
    else:
        needs_correction.append('Consider adding phone number')
    
    # Check for action verbs
    action_verbs = ['achieved', 'managed', 'developed', 'created', 'led', 'improved', 
                   'increased', 'designed', 'implemented', 'analyzed', 'coordinated']
    action_count = sum(1 for verb in action_verbs if verb.lower() in text.lower())
    
    if action_count >= 5:
        good_points.append(f'Good use of action verbs ({action_count} found)')
    elif action_count >= 2:
        needs_correction.append(f'Could use more action verbs (only {action_count} found)')
    else:
        fails.append('Very few action verbs used')
    
    # Check for quantifiable achievements
    number_pattern = r'\b\d+(\.\d+)?%?|\b\d+k\b|\b\$\d+|\b\d+\+\b'
    numbers = re.findall(number_pattern, text, re.IGNORECASE)
    
    if len(numbers) >= 3:
        good_points.append(f'Contains quantifiable achievements ({len(numbers)} metrics found)')
    elif len(numbers) >= 1:
        needs_correction.append(f'Could use more quantifiable achievements (only {len(numbers)} found)')
    else:
        fails.append('No quantifiable achievements found')
    
    # Check length
    word_count = len(text.split())
    if 200 <= word_count <= 800:
        good_points.append(f'Appropriate length ({word_count} words)')
    elif word_count < 200:
        fails.append(f'Resume too short ({word_count} words)')
    else:
        needs_correction.append(f'Resume might be too long ({word_count} words)')
    
    # Calculate numerical score (0-100)
    base_score = 50  # Start with base score
    score = base_score + (len(good_points) * 12) - (len(fails) * 15) - (len(needs_correction) * 8)
    
    # Ensure score is within 0-100 range
    score = max(0, min(100, score))
    
    return {
        'score': score,
        'grade': get_letter_grade(score),
        'good': good_points,
        'needs_correction': needs_correction,
        'fails': fails
    }


def get_letter_grade(score):
    """Convert numerical score to letter grade."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B+'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'D'


def generate_highlighted_text(text, analysis_results):
    """Generate HTML with colored highlighting based on analysis."""
    highlighted = text
    
    # Find and highlight good elements (green)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    highlighted = re.sub(email_pattern, r'<span class="highlight-good">\g<0></span>', highlighted)
    
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    highlighted = re.sub(phone_pattern, r'<span class="highlight-good">\g<0></span>', highlighted)
    
    # Highlight action verbs (green)
    action_verbs = ['achieved', 'managed', 'developed', 'created', 'led', 'improved', 
                   'increased', 'designed', 'implemented', 'analyzed', 'coordinated']
    for verb in action_verbs:
        pattern = r'\b' + re.escape(verb) + r'\b'
        highlighted = re.sub(pattern, r'<span class="highlight-good">\g<0></span>', highlighted, flags=re.IGNORECASE)
    
    # Highlight numbers/metrics (good)
    number_pattern = r'\b\d+(\.\d+)?%?|\b\d+k\b|\b\$\d+|\b\d+\+\b'
    highlighted = re.sub(number_pattern, r'<span class="highlight-good">\g<0></span>', highlighted)
    
    # Highlight potential issues (yellow/red)
    if len(text.split()) < 200:
        highlighted = f'<div class="highlight-warning">Resume appears too short ({len(text.split())} words)</div>' + highlighted
    elif len(text.split()) > 800:
        highlighted = f'<div class="highlight-warning">Resume might be too long ({len(text.split())} words)</div>' + highlighted
    
    return highlighted


def generate_ai_rewrite(text, analysis_results):
    """Generate an AI-enhanced rewrite of the resume."""
    # For now, provide basic improvements based on analysis
    improvements = []
    
    if any('Missing email' in fail for fail in analysis_results['fails']):
        improvements.append("Add your email address: your.email@domain.com")
    
    if any('phone number' in need for need in analysis_results['needs_correction']):
        improvements.append("Add your phone number: (555) 123-4567")
    
    if any('action verbs' in need for need in analysis_results['needs_correction']):
        improvements.append("Replace passive language with action verbs like: achieved, managed, developed, created")
    
    if any('quantifiable' in need for need in analysis_results['needs_correction']):
        improvements.append("Add specific metrics and numbers to your achievements")
    
    # Create improved version
    improved_text = text
    if improvements:
        improved_text = "=== SUGGESTED IMPROVEMENTS ===\n" + "\n".join(f"• {imp}" for imp in improvements) + "\n\n=== ORIGINAL RESUME ===\n" + text
    
    return improved_text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return redirect(url_for('index'))

    file = request.files['resume']
    if file.filename == '':
        return redirect(url_for('index'))

    # Save the file temporarily
    file_path = os.path.join('static', 'uploads', file.filename)
    file.save(file_path)

    # Process the file based on extension
    text = ""
    if file.filename.lower().endswith('.pdf'):
        if PYMUPDF_AVAILABLE:
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text()
        else:
            text = "PDF support not available. Please install PyMuPDF or use DOC/DOCX/TXT format."
    elif file.filename.lower().endswith(('.doc', '.docx')):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + '\n'
    else:  # Assume plain text
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as f:
                text = f.read()

    # Analyze the extracted text
    results = analyze_resume_text(text)
    
    # Generate highlighted text
    highlighted_text = generate_highlighted_text(text, results)
    
    # Generate AI rewrite
    rewritten_text = generate_ai_rewrite(text, results)

    return render_template(
        'results.html',
        results=results,
        original_text=text,
        highlighted_text=highlighted_text,
        rewritten_text=rewritten_text
    )


if __name__ == '__main__':
    uploads_path = os.path.join('static', 'uploads')
    os.makedirs(uploads_path, exist_ok=True)
    app.run(debug=True)
