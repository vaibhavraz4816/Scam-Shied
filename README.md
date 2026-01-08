🛡️ Scam-Shield


AI-Powered Scam & Phishing Detection System


Scam-Shield is a professional 
Python-based web application designed to detect fraudulent, phishing, 
and scam messages using OCR (Computer Vision) and Generative AI (NLP). 
Users upload a screenshot of suspicious SMS, WhatsApp, or Email 
messages, and the system generates a risk score, identifies red flags, 
and provides safety recommendations.


This project is developed as a problem-solving MCA final year project with strong real-world cybersecurity relevance.



🚨 Problem Statement


With the rapid increase in digital communication, users are frequently targeted by scams such as:


• Fake electricity disconnection messages

• Bank KYC or account block warnings

• Fraudulent payment links and QR codes

• Prize, lottery, and impersonation scams


Even educated users fall victim due 
to urgency, fear, and psychological manipulation. Traditional rule-based
 filters are insufficient to detect evolving scam patterns.



💡 Proposed Solution


Scam-Shield provides an AI-driven cybersecurity decision support system that works as follows:




User uploads a screenshot of a suspicious message




OCR extracts text from the image




Generative AI analyzes scam intent and manipulation patterns




System generates:




Risk Score (0–100)




Verdict (Safe / Suspicious / High Risk Scam)




Detected Red Flags




Actionable Safety Advice







🧠 Core Problem-Solving Aspects


• Computer Vision: Converting unstructured image data into readable text

• Natural Language Processing: Identifying scam intent and urgency

• Cybersecurity Logic: Risk classification and response guidance

• System Design: Modular backend architecture using FastAPI



🏗️ System Architecture


User Screenshot

↓

OCR Module (EasyOCR)

↓

Extracted Text

↓

AI Analysis Engine (Google Gemini)

↓

Risk Score, Verdict & Safety Advice

↓

Web Interface (FastAPI + HTML/CSS)



🧪 Technology Stack


Backend: FastAPI (Python)

Frontend: HTML + CSS (Jinja Templates)

OCR Engine: EasyOCR

AI Model: Google Gemini (Generative AI)

Image Processing: Pillow, NumPy

Server: Uvicorn



📁 Project Structure


scam-shield/


app/

main.py – FastAPI entry point

ocr.py – OCR logic

ai_analysis.py – AI-based scam detection

templates/index.html – Frontend UI

static/style.css – Styling


requirements.txt – Dependencies

README.md – Documentation

.env – API key (ignored by Git)

.gitignore – Git ignore rules



🔐 API Key Configuration


Create a .env file in the project root and add:


GOOGLE_API_KEY=your_api_key_here


The API key is securely loaded using environment variables and is not committed to GitHub.



🚀 Installation & Running the Project




Clone the repository

git clone https://github.com/your-username/scam-shield.git

cd scam-shield




Create virtual environment

python -m venv venv

venv\Scripts\activate   (Windows)

source venv/bin/activate   (Linux/macOS)




Install dependencies

pip install -r requirements.txt




Run the application

uvicorn app.main:app --reload




Open in browser

http://127.0.0.1:8000





📱 How to Use




Take a screenshot of a suspicious SMS, WhatsApp, or Email




Upload the image on the web interface




OCR extracts the text




AI analyzes scam indicators




Review risk score and safety recommendations





🧪 Sample Test Cases


Electricity Scam:

“Your electricity will be disconnected tonight. Pay immediately.”


Bank KYC Scam:

“KYC pending. Update within 2 hours or account will be blocked.”


Prize Scam:

“Congratulations! You have won ₹50,000. Claim now.”



🔮 Future Enhancements


• Multi-language support (Indian regional languages)

• Rule-based fallback detection without AI

• Browser extension for real-time detection

• Mobile application (Flutter / React Native)

• QR code and URL reputation analysis

• Scam reporting and community database



🎓 Academic Relevance


Degree: MCA (Final Year Project)

Domain: Cybersecurity & Artificial Intelligence

Focus Areas:

• Problem solving

• Real-world applicability

• Secure system design

• AI-assisted decision making



⚠️ Disclaimer


This tool is developed for 
educational and awareness purposes only. While AI provides strong 
indicators, users should always verify information through official 
channels, never share OTPs or passwords, and report scams to cybercrime 
authorities.



👨‍💻 Author

Vaibhav Raaj Singh

Scam-Shield

MCA Final Year Project

Domain: Cybersecurity & AI
