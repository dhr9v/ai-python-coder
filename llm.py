import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def get_code(system_prompt, user_prompt):
    full_prompt = f"""
{system_prompt}

User request:
{user_prompt}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",   
        contents=full_prompt,
        config=types.GenerateContentConfig(
            temperature=0.3
        )
    )

    return response.text
