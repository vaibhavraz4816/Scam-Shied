import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_scam(text: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a Cybersecurity Analyst.

Analyze the following message for scam or phishing risk.

Message:
"{text}"

Respond strictly in this format:

Risk Score: (0–100)
Verdict: Safe / Suspicious / High Risk Scam
Red Flags:
- Point 1
- Point 2
- Point 3
Safety Advice:
- What should the user do now
"""

    response = model.generate_content(prompt)
    return response.text
