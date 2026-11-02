import os
import time
import json

from google import genai
from dotenv import load_dotenv 
from google.genai import types

load_dotenv()
GEMINI_API_KEY=os.getenv("GMINI_API_KKEY")

if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY not found")

client=genai.Client(api_key=GEMINI_API_KEY)
ping=client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Reply with exactly three words:API key words."
)
print("[ping]{ping.text.strip()}")