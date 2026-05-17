from google import genai
import json

## put your api key here, don't just run with key
client = genai.Client(api_key="key")


## This func contains the promp that would analyze and retun a json
## param = text->text that is extracted from the file 
## return = json of all the skills that are in here
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
    try:
        parsed = json.loads(response.text)
        return parsed
    except json.JSONDecodeError:# this is just doing it again if gemnai messes up 
        fix_response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=f"""
    Fix this output into VALID JSON ONLY.

    Return ONLY this structure:
    {{
    "skills": [],
    "strengths": [],
    "weaknesses": [],
    "suggestions": [],
    "score": 0
    }}

    Do NOT add explanations. Do NOT change keys.

    Bad output:
    {response.text}
    """
        )

        try:
            return json.loads(fix_response.text)

        except json.JSONDecodeError:#returing a empty json if all operations fail
            return {
                "skills": [],
                "strengths": [],
                "weaknesses": [],
                "suggestions": [],
                "score": 0
            }

