from google.genai.types import HttpOptions
from google import genai
import os

chaveAPI = os.getenv("GEMINI_API_KEY")

client = genai.Client(http_options=HttpOptions(api_version="v1"))

class responses:
    
    @staticmethod
    def normalResponse(question: str):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question,
        )
        
        return response.candidates[0].content.parts[0].text