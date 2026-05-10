from google import genai
import json


client = genai.Client(api_key="AIzaSyDCzVbjEc2druCI0Wx8ylRqks6sIxxbs2E")

def ai_analyze():
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"""
        if this is working, telling what is call about apples in 50 words

        """
    )
    parsed = response.text
    return parsed
