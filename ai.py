from google import genai
import json


client = genai.Client(api_key="key")

def ai_analyze(text):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"""
        if this is working, telling what is call about apples in 50 words
        """
    )