# ResumeRocket - AI Resume Analyzer

## 🚀 Project Overview

ResumeRocket is an AI-powered resume analyzer that helps job seekers optimize their resumes for ATS (Applicant Tracking System) compatibility. The application provides intelligent feedback, visual highlighting, and generates professionally formatted improved versions of resumes.

## ✨ Features

- **Multi-format Support**: Upload PDF, DOC, DOCX, or TXT files
- **AI-Powered Analysis**: Intelligent resume analysis with industry keyword detection
- **ATS Scoring**: 0-100 numerical scoring system with letter grades
- **Visual Highlighting**: Color-coded feedback on resume content
- **Professional Rewrite**: AI-generated improved resume versions
- **Multiple Download Formats**: Export as TXT, PDF, or DOCX
- **Mobile-Responsive Design**: Optimized for all screen sizes
- **Professional Branding**: Clean, modern interface with ResumeRocket identity

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Document Processing**: PyMuPDF, python-docx, ReportLab
- **Deployment**: Netlify Functions
- **Styling**: Mobile-first responsive design

## 📁 Project Structure

```
Resume Analyzer/
├── resume_analyzer/
│   ├── functions/
│   │   └── app.py              # Netlify Functions handler
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css      # Main styling
│   │   ├── js/
│   │   │   └── script.js       # Frontend functionality
│   │   └── uploads/            # Temporary file storage
│   ├── templates/
│   │   ├── index.html          # Main upload page
│   │   └── results.html        # Analysis results page
│   ├── app.py                  # Main Flask application
│   ├── requirements.txt        # Python dependencies
│   ├── runtime.txt            # Python version specification
│   ├── Procfile               # Process configuration
│   └── netlify.toml           # Netlify configuration
├── TODO.md                    # Project tracking
├── ACTIONS.md                 # Action items log
├── SUMMARY.md                 # Project summary
└── README.md                  # This file
```

## 🚀 Deployment to Netlify

### Prerequisites

1. GitHub account
2. Netlify account (free tier available)
3. Git installed locally

### Deployment Steps

1. **Prepare Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - ResumeRocket app"
   ```

2. **Push to GitHub**
   - Create a new repository on GitHub
   - Push your local repository:
   ```bash
   git remote add origin https://github.com/yourusername/resume-rocket.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Netlify**
   - Log in to [Netlify](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Connect your GitHub account
   - Select your resume-rocket repository
   - Configure build settings:
     - Build command: `pip install -r resume_analyzer/requirements.txt`
     - Publish directory: `resume_analyzer`
     - Functions directory: `resume_analyzer/functions`

4. **Environment Configuration**
   - Python version: 3.11 (specified in runtime.txt)
   - Dependencies automatically installed from requirements.txt

### Environment Variables (if needed)

For production deployment, you may want to set:
- `FLASK_ENV=production`
- Any API keys for AI services (if integrated)

## 💻 Local Development

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resume-rocket.git
   cd resume-rocket/resume_analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open http://localhost:5000 in your browser

### Development Commands

- **Install new dependency**: Add to requirements.txt and run `pip install -r requirements.txt`
- **Test PDF generation**: Ensure ReportLab is installed properly
- **Debug mode**: Set `debug=True` in app.py for development

## 📊 Features Implemented

### Core Functionality
- ✅ Multi-format file upload (PDF, DOC, DOCX, TXT)
- ✅ AI-powered resume analysis
- ✅ 0-100 ATS scoring system
- ✅ Visual text highlighting
- ✅ Professional resume rewriting
- ✅ Multiple download formats

### UI/UX Enhancements
- ✅ Mobile-first responsive design
- ✅ Professional dark theme with ResumeRocket branding
- ✅ File upload feedback (icon changes on selection)
- ✅ Animated instructions and smooth transitions
- ✅ Professional document formatting

### Technical Improvements
- ✅ Robust error handling and file validation
- ✅ Clean code structure and documentation
- ✅ Emoji removal from professional output
- ✅ Realistic metrics in suggestions
- ✅ Proper heading formatting (no unwanted bullet points)
- ✅ Netlify deployment configuration

## 🔧 Configuration Files

### netlify.toml
Configures Netlify Functions deployment with Python 3.11 runtime.

### requirements.txt
Contains all Python dependencies with specific versions for stable deployment.

### Procfile
Specifies the web process for deployment platforms.

### runtime.txt
Specifies Python version for deployment consistency.

## 🎯 Production Ready

The application is fully production-ready with:
- Professional code structure
- Comprehensive error handling
- Mobile-responsive design
- Scalable architecture
- Clean deployment configuration

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues or questions, please create an issue in the GitHub repository.
