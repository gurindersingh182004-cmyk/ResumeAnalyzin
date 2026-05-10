from google import genai
import json


client = genai.Client(api_key="key")

def ai_analyze(text):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=f"""
        You are a resume analyzer.You are a strict JSON generator.
        You MUST return ONLY valid JSON.
        Do NOT include any explanations, text, or formatting outside JSON.      

       {{
        "skills": ["string"],
        "strengths": ["string"],
        "weaknesses": ["string"],
        "suggestions": ["string"],
        "score": number
       }}

        Rules:
        - Always return all keys.
        - If no data exists, return empty arrays [].
        - score must be between 0 and 100.
        - Output must be valid JSON that can be parsed directly.

        Resume:
        {text}
        
        """
    )
    parsed = response.text
    return parsed
