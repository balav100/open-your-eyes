# open-your-eyes
# 👁️ Open Your Eyes

### AI-Powered Braille Accessibility & Learning Platform

Open Your Eyes is an NLP-driven accessibility platform designed to help visually impaired users access digital books more effectively. The application converts uploaded PDF/TXT books into Braille text, generates audio narration, provides AI-powered summaries, evaluates readability, and offers an AI Tutor that explains book content in both plain text and Braille format.

---

## 🚀 Features

### 📚 Document Upload
- Upload PDF books
- Upload TXT files
- Automatic text extraction

### 🌍 Language Detection
- Detects the language of uploaded content
- Supports multilingual documents

### 📝 Text Preview
- Displays extracted and cleaned text
- Enables users to verify content before conversion

### ⠃ Braille Conversion
- Converts text into Unicode Braille representation
- Real-time Braille preview panel

### 📖 Accessibility Score Meter
- Evaluates readability level
- Classifies content as:
  - Easy
  - Medium
  - Advanced

### 🤖 AI Smart Summary
- Generates concise summaries of lengthy books
- Helps users quickly understand key concepts

### 🎓 AI Tutor
- Answers user questions about uploaded books
- Explains difficult concepts in simple language
- Generates explanations in Braille format

### 🔊 Audio Narration
- Converts book content into speech
- Accessible audio playback directly in the application

### 📥 Export Options
- Download Braille book as TXT
- Download Braille book as PDF

---

## 🏗️ System Architecture

```text
User Upload
      │
      ▼
Text Extraction
      │
      ▼
Text Cleaning
      │
      ▼
Language Detection
      │
      ▼
Braille Conversion
      │
      ├────────► Braille Preview
      │
      ├────────► PDF Export
      │
      └────────► TXT Export

      ▼
Readability Analysis
      ▼
Smart Summary
      ▼
AI Tutor
      ▼
Audio Narration
```

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Natural Language Processing
- Transformers
- Hugging Face Models

### OCR & Document Processing
- EasyOCR
- PDFPlumber
- PyMuPDF

### Audio Generation
- gTTS

### Accessibility Processing
- Unicode Braille Mapping

### Utilities
- Python
- TextStat
- LangDetect

---

## 📂 Project Structure

```text
open-your-eyes/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── modules/
│   ├── ai_tutor.py
│   ├── audio_generator.py
│   ├── braille_converter.py
│   ├── language_detector.py
│   ├── pdf_extractor.py
│   ├── pdf_generator.py
│   ├── readability.py
│   ├── summarizer.py
│   ├── text_cleaner.py
│   └── utils.py
│
├── assets/
│   └── DejaVuSans.ttf
│
├── uploads/
└── outputs/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/open-your-eyes.git
cd open-your-eyes
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 🎯 Target Users

- Visually impaired readers
- Students requiring accessible learning materials
- Educational institutions
- Accessibility researchers
- NGOs supporting inclusive education

---

## 💡 Real-World Impact

Millions of visually impaired individuals face challenges accessing digital educational content. Open Your Eyes bridges this gap by transforming conventional digital books into accessible Braille and audio formats while leveraging AI to enhance comprehension and learning.

---

## 🔮 Future Enhancements

- Multi-language Braille support
- OCR-based image-to-Braille conversion
- Personalized learning analytics
- Braille authentication system
- Voice-controlled navigation
- Graph-RAG powered knowledge exploration
- Cloud storage integration

---

## 📊 Key Highlights

- Accessibility-Focused AI Solution
- NLP-Based Educational Assistant
- Braille Conversion Engine
- AI Tutor Integration
- Audio Narration Support
- Downloadable Braille Documents
- Inclusive Learning Platform

---

## 👨‍💻 Author

**Balasubramaniam V**

B.Tech Computer Science Engineering

Interested Roles:
- Data Scientist
- NLP Engineer
- AI Automation Engineer
- Generative AI Engineer

GitHub: https://github.com/balav100

LinkedIn: https://linkedin.com/in/Balasubramaniam V
