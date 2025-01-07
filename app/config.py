import os

class Config:
    CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
